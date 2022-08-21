# Import necessary libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 
from tqdm import tqdm
import warnings 
from ast import literal_eval
warnings.filterwarnings('ignore')


from scipy import stats
from ast import literal_eval
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.metrics.pairwise import linear_kernel, cosine_similarity
from nltk.stem.snowball import SnowballStemmer

metadata=pd.read_csv("/Users/shreejamehta/movierecomsystem/movies_metadata.csv")

pd.DataFrame(metadata.isnull().sum()/(metadata.shape[0])*100)

credit=pd.read_csv("/Users/shreejamehta/movierecomsystem/credits.csv")
keyword=pd.read_csv("/Users/shreejamehta/movierecomsystem/keywords.csv")

metadata = metadata.drop([19730, 29503, 35587])
keyword['id'] = keyword['id'].astype('int')
credit['id'] = credit['id'].astype('int')
metadata['id'] = metadata['id'].astype('int')
metadata=metadata.merge(credit,on='id')
metadata=metadata.merge(keyword,on='id')

metadata['cast']=metadata['cast'].apply(literal_eval)
metadata['crew'] = metadata['crew'].apply(literal_eval)
metadata['keywords'] = metadata['keywords'].apply(literal_eval)

metadata['cast_size']=metadata['cast'].apply(lambda x:len(x))
metadata['crew_size']=metadata['crew'].apply(lambda x:len(x))

def get_director(x):
    for i in x:
        if i['job']=='Director':
            return i['name']
    return np.nan
metadata['director']=metadata['crew'].apply(get_director)
metadata['cast'] = metadata['cast'].apply(lambda x: [i['name'] for i in x] if isinstance(x, list) else [])
metadata['cast'] = metadata['cast'].apply(lambda x: x[:3] if len(x) >=3 else x)

metadata['keywords'] = metadata['keywords'].apply(lambda x: [i['name'] for i in x] if isinstance(x, list) else [])

metadata['cast']=metadata['cast'].apply(lambda x:[str.lower(i.replace(" ","")) for i in x])
metadata['director']=metadata['director'].astype('str').apply(lambda x : x.replace(" ",""))
metadata['director']=metadata['director'].apply(lambda x:[x,x,x])

s=metadata.apply(lambda x:pd.Series(x['keywords']),axis=1).stack().reset_index(level=1,drop=True)
s.name='keyword'
s=s.value_counts()
s=s[s>1]

def filter_keywords(x):
    words = []
    for i in x:
        if i in s:
            words.append(i)
    return words

stemmer = SnowballStemmer('english')
metadata['keywords'] = metadata['keywords'].apply(filter_keywords)
metadata['keywords'] = metadata['keywords'].apply(lambda x: [stemmer.stem(i) for i in x])
metadata['keywords'] = metadata['keywords'].apply(lambda x: [str.lower(i.replace(" ", "")) for i in x])

metadata['genres'] = metadata['genres'].fillna('[]').apply(literal_eval).apply(lambda x: [i['name'] for i in x] if isinstance(x, list) else [])

list_=[]
def genre_vis(x):
    for i in x:
        for j in i:
            list_.append(j)
genre_vis(metadata['genres'])

ge=pd.Series(list_)

metadata['soup'] = metadata['keywords'] + metadata['cast'] + metadata['director'] + metadata['genres']
metadata['soup'] = metadata['soup'].apply(lambda x: ' '.join(x))

count = CountVectorizer(analyzer='word',ngram_range=(1, 2),min_df=0, stop_words='english')
count_matrix = count.fit_transform(metadata['soup'])
cosine_sim = cosine_similarity(count_matrix, count_matrix)

smd = metadata.reset_index()
titles = metadata['title']
indices = pd.Series(metadata.index, index=metadata['title'])

def get_recommendations(title):
    idx = indices[title]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:31]
    movie_indices = [i[0] for i in sim_scores]
    return titles.iloc[movie_indices]

print(get_recommendations('Jumanji').head(10))