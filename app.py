from flask import Flask,render_template,request
# from final_edit import get_recommendations
from hybrid import predict_movies,generate_cosine_tfidf,top_movies

app= Flask(__name__)

@app.route('/',methods=['GET'])
def man():
    return render_template('index.html')

@app.route('/predict', methods=['GET','POST'])
def home():
    moviename= request.form['movie']
    movies = top_movies(2000)
    tf_idf = generate_cosine_tfidf(movies, alpha = 0.6)
    pred= predict_movies(moviename, num=6, verbose =2, out =True, data= movies, tf_idf = tf_idf)
    names=[]
    genres=[]
    links=[]
    for i in range(len(pred)):
         names.append(pred.iloc[i][0])
         genres.append(pred.iloc[i][2])
         links.append(pred.iloc[i][3])
    return render_template('prediction.html', movie_names=names, movie_genres= genres, movie_links= links, moviename=moviename)

if __name__ == '__main__':
    app.run(debug=True)