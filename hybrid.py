import pandas as pd
import numpy as np
import re
from sklearn.metrics.pairwise import cosine_similarity
from nltk.corpus import stopwords
stopwords_english = set(stopwords.words('english'))
from nltk.stem import PorterStemmer
stemmer = PorterStemmer()
from ast import literal_eval


import warnings
warnings.filterwarnings("ignore")
data = pd.read_csv('movies_metadata.csv', low_memory = False)[['id','original_title', 'imdb_id', 'genres', 'overview', 'vote_average', 'vote_count']].dropna().set_index('id')
credits = pd.read_csv('credits.csv', low_memory = False).set_index('id').dropna()

def split_genres(row):
    row['genres'] = " ".join([info['name'] for info in literal_eval(row['genres'])])
    return row
data = data.apply(split_genres, axis=1)

def find_director(row):
    try:
        for info in literal_eval(row['crew']):
            if info['job'] == 'Director':
                row['director'] = info['name']
                break
    except:
        row['director'] = pd.NA
    return row
credits = credits.apply(find_director, axis=1).drop(['cast', 'crew'], axis=1)
credits.index = credits.index.astype(str)


data = pd.merge(data, credits, left_index = True, right_index = True, how = 'left')
data.index = data.index.astype(int)


def top_movies(num = 100, quantile = 0.95, data = data):
    req_votes = np.quantile(data['vote_count'], quantile)
    
    new_data = data[data['vote_count']>req_votes]
    means = new_data['vote_average']
    tot_mean = new_data['vote_average'].mean()
    votes = new_data['vote_count']
    
    new_data['ratings'] = (votes/(votes+req_votes)*means + req_votes/(votes+req_votes)*tot_mean)
    
    return new_data.sort_values('ratings', ascending = False).iloc[:num,:].reset_index(drop=True)

def clean(x):
    res = []
    for w in x:
        if w not in stopwords_english:
            w = stemmer.stem(re.sub('[^a-zA-z0-9]', '', w))
            if(len(w)>0):
                res.append(w)
    return res

def preprocess(data):
    stemmer = PorterStemmer()
    docs = []
    DF = {}
    
    for ind, row in data.iterrows():
        set_title = set()
        doc_count = 0
        title = row['original_title'].lower().strip().split()
        title += row['genres'].lower().strip().split()
        title += [row['director'].lower().strip()]
        body = row['overview'].lower().strip().split()
        body = clean(body)
        
        for word in title+body:
            if word in DF:
                if row.name in DF[word]:
                    DF[word][row.name]+=1
                else:
                    DF[word][row.name] = 1
            else:
                DF[word] = {}
                DF[word][row.name] = 1
            
            doc_count+=1
            if word in title:
                set_title.add(word)
        docs.append((doc_count, set_title))

    return DF, docs

def generate_cosine_tfidf(data, alpha = 0.6):
    DF, docs = preprocess(data)
    tf_idf = np.zeros((len(docs), len(DF)))
    
    for i, (word, key) in enumerate(DF.items()):
        w_count = np.sum([value for _, value in key.items()])
        for ind, value in key.items():
            tf = value/docs[ind][0]
            idf = np.log(len(docs)/(w_count+1))
            tfidf = tf*idf*(1-alpha)
            if word in docs[ind][1]:
                tfidf = tf*idf*alpha
            
            tf_idf[ind][i] = tfidf
    return cosine_similarity(tf_idf)

movies = top_movies(500)
tf_idf = generate_cosine_tfidf(movies, alpha = 0.6)

def predict_movies(movie_name = "The Dark Knight", num = 10, verbose = 0, out = True, data = movies, tf_idf = tf_idf):
    try:
        ind = data[data['original_title'] == movie_name].index[0]
        output = data.loc[[val for val in np.argsort(tf_idf[ind])[::-1][1:num+1]]]
        if verbose <1:
            print("The TF-IDF Cosine similarity scores for relevant movies are as follows:\n")
            print([round(val,2) for val in np.sort(tf_idf[ind])[::-1][1:num+1]], '\n')
        if verbose >= 1:
            print(f'The top {num} recommended movies for "{movie_name}" are as follows:\n')
            for ind, row in output.iterrows():
                print("Title: {}".format(row['original_title']))
                print("Rating: {}".format(round(row['ratings'], 1)))
                print("Genres: {}".format(row['genres']))
                print("IMDB Link: https://www.imdb.com/title/{}".format(row['imdb_id']))
                print("*****************************************************\n")

        if(out):
            return output
    except:
        print("MOVIE NOT FOUND!")

movies = top_movies(45000)
tf_idf = generate_cosine_tfidf(movies, alpha = 0.6)

#print(predict_movies("Moana", num = 10, verbose = 0, out = True, data = movies, tf_idf = tf_idf))

predict_movies("The Dark Knight", num = 10 , verbose = 2, out = False, data = movies, tf_idf = tf_idf)
