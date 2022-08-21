import pandas as pd
import numpy as np


meta = pd.read_csv('movies_metadata.csv', low_memory = False)
meta = meta[ ['id', 'original_title', 'original_language', 'genres'] ]

meta = meta.rename(columns={'id':'movieId',
'original_title': 'title',
'original_language': 'language'})

meta = meta.loc[meta['language'] == 'en',:]

meta.movieId = pd.to_numeric(meta.movieId)

def str_to_set(x):
    genre_set = set()
    for item in eval(x):
        genre_set.add(item['name'])
    return genre_set

meta.genres = meta.genres.apply(str_to_set)

keywords = pd.read_csv('keywords.csv')

keywords['keywords'] = keywords['keywords'].apply(str_to_set)

keywords = keywords.rename(columns={'id': 'movieId'})
keywords.movieId = pd.to_numeric(keywords.movieId)

meta = pd.merge(meta, keywords, on='movieId', how='inner')

dk = meta[meta['title']=='The Dark Knight'].iloc[0,:]
dkr = meta[meta['title']=='The Dark Knight Rises'].iloc[0,:]
pd.concat([dk, dkr], axis = 1).T

dk = meta[meta['title']=='The Dark Knight'].iloc[0,:]
dkr = meta[meta['title']=='The Dark Knight Rises'].iloc[0,:]
pd.concat([dk, dkr], axis = 1).T

def jaccard_similarity(s1, s2):
    if len(s1|s2) == 0:
        return 0
    return len(s1&s2)/len(s1|s2)

jaccard_similarity(dk.genres|dk.keywords, dkr.genres|dkr.keywords)

ratings = pd.read_csv( 'ratings_small.csv')

ratings.movieId = pd.to_numeric(ratings.movieId)

ratings = pd.merge(ratings, meta[['movieId', 'title']], on='movieId', how='inner')

matrix = ratings.pivot_table(index= 'userId', columns='title', values='rating')

def pearson_similarity(u1, u2):
    u1_c = u1 - u1.mean()
    u2_c = u2 - u2.mean()
    denom = np.sqrt(np.sum(u1_c ** 2) * np.sum(u2_c ** 2))
    if denom != 0:
        return np.sum(u1_c * u2_c)/denom
    else:
        return 0

dk_rating = matrix['The Dark Knight']
pk_rating = matrix['Prom Night']
pearson_similarity(dk_rating, pk_rating)

def find_similar_movies (input_title , matrix, n, alpha):
    input_meta = meta.loc[ meta['title'] == input_title].iloc[0]
    input_set = input_meta.genres | input_meta.keywords
 
    result = []
 
    for this_title in matrix.columns:
        if this_title == input_title:
            continue
        this_meta = meta.loc[ meta['title'] == this_title].iloc[0]
        this_set = this_meta.genres | this_meta.keywords
 
        pearson = pearson_similarity(matrix[this_title], matrix[input_title])
        jaccard = jaccard_similarity(this_set, input_set)
 
        marks = alpha * pearson + (1-alpha) * jaccard
        score = format(marks, '.2f')
        result.append( (this_title, pearson, jaccard, score) )
 
    result.sort(key= lambda r: r[3], reverse= True)
    
    return result[:n]

result = find_similar_movies('The Dark Knight', matrix, 10, 0.3)
final = pd.DataFrame(result, columns = ['title', 'pearson', 'jaccard', 'score'])
final_score = final.score
score_list = final_score.values.tolist()
# print(final)
# print("\n")
# score_arr = final_score.to_numpy()
# print(score_arr)
# print("\n")
# print(score_list)