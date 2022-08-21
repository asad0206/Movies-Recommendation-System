import math  
import numpy as np  
import sklearn.metrics
from validate import *
from hybrid import *
from sklearn.metrics import mean_squared_error

# actual = [0.43, 0.30, 0.29, 0.25, 0.24, 0.15, 0.14, 0.14, 0.13, 0.13]  
# predic = [0.2546504255695188, 0.24762533596378403, 0.20638253129365067, 0.2006433534933286, 0.19131835172791867, 0.18993007550517704, 0.18555714659677686, 0.17839466013927857, 0.17302485016263758, 0.17039881149803363]
# Mse = mean_squared_error(actual,predic)
# Rsme = math.sqrt(Mse)
# print("MSE:  ", Mse)
# print("RMSE: ", Rsme)
  
#finding TF-IDF recommendation based cosine similarity scores 
movies = top_movies(5000)
tf_idf = generate_cosine_tfidf(movies, alpha = 0.6)
predict= predict_movies("The Dark Knight", num=10, verbose =0, out =True, data= movies, tf_idf = tf_idf)

#finding Scores using pearson-jaccard similarity 
result = find_similar_movies('The Dark Knight', matrix, 10, 0.3)
final = pd.DataFrame(result, columns = ['title', 'pearson', 'jaccard', 'score'])

#storing a single column from pandas dataframe
final_score = final.score

#converting pandas dataframe to list
score_list = final_score.values.tolist()
print("The coefficient for relevant movies are as follows:")
print(score_list)
actual = score_list

#finding the deviation
Mse = mean_squared_error(actual,predict)
Rsme = math.sqrt(Mse)
print('MSE:  ', Mse) #Mean Squared Error
print("RMSE: ", Rsme) #Root Mean squared error