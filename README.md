**PROJECT BASED LEARNING - I REPORT
ON
MOVIE RECOMMENDATION SYSTEM**
===================================

## **REPORT SUBMITTED TOWARDS PARTIAL FULFILLMENT OF THE REQUIREMENT FOR THE AWARD OF THE DEGREE OF**

**BACHELOR OF TECHNOLOGY**

**IN
COMPUTER SCIENCE AND ENGINEERING**

**SUBMITTED BY-**

**MD ASAD ANSARI (20070122075)
SHREEJA PRATIK MEHTA (20070122076)
NILESH KUMAR (20070122086)
PRANAV PRASANTH NARANATT (20070122098)**

![https://www.google.com/a/cpanel/sitpune.edu.in/images/logo.gif?service=google_gsuite](/README/Aspose.Words.b3b2922a-bbea-468d-8499-819230b179f7.001.jpeg)

**Under the Guidance of
Dr. Anupkumar M Bongale**

**SYMBIOSIS INSTITUTE OF TECHNOLOGY
(A CONSTITUENT OF SYMBIOSIS INTERNATIONAL UNIVERSITY)**

**Pune – 412115**
SYMBIOSIS INSTITUTE OF TECHNOLOGY, 2021-2022

` `XV
![](/README/Aspose.Words.b3b2922a-bbea-468d-8499-819230b179f7.002.png)

## **CERTIFICATE**

The project titled “**Movie Recommendation System”** submitted to the Symbiosis Institute of Technology, Pune for the second-year project in **Computer Science and Engineering** is based on our original work carried out under the guidance of **Dr. Anupkumar M Bongale**. The report has not been submitted elsewhere for the award of any degree or for any other research related activity.

The material borrowed from other sources and incorporated in the report has been duly acknowledged and/or referenced.

We understand that we could be held responsible and accountable for plagiarism, if any, detected later.

Date: **Signature of the candidate**

**Research Guide Head of the Department**

(Dr. Anupkumar M Bongale) (Dr. Deepali Vora)

# **ACKNOWLEDGEMENT**

It gives us great pleasure presenting the preliminary project report on “**Movie Recommendation System**”.

I would like to take this opportunity to thank my internal guide, Dr. Anupkumar M Bongale, for giving us all the help and guidance we needed. I am grateful to them for their kind support. Their valuable suggestions were very helpful.

I am also grateful to Dr. Deepali Vora, Head of Department, SIT, Pune for her indispensable support, suggestions.

In the end our special thanks to Symbiosis Institute of Technology for providing various resources such as laboratories with all needed software platforms, continuous Internet connection, for our Project.

Md Asad Ansari (20070122075)

Shreeja Pratik Mehta (20070122076)

Nilesh Kumar (20070122086)

Pranav Prasanth Naranatt (20070122098)

## **ABSTRACT**

Recommender systems are a subclass of information filtering that** attempts to predict the ratings and** likes that user give to an item. Commonly used recommender systems include playlist generators for video and music services, product recommenders for online enterprises, content recommenders for social media platforms, and open web content. These systems work with a single input such as music, or multiple inputs within and between platforms such as news, books, and search. Popular recommender systems for specialized themes such as restaurants and online dating, research articles, experts, staff, and recommender systems for investigating financial services have also been developed. These systems make use of various methods of filtering such as content-based filtering (filtering method in which recommendations are made using the contents of the database) or collaborative filtering (filtering method in which recommendations are made from the likes and ratings given by the user) as well as other systems such as knowledge-based systems. Each of these systems has its strengths and weaknesses.

# **Table of Contents**

1. [Introduction 1](#_TOC_250000)
   1. Overview… 1
   1. The Goals 1
   1. Problem Statement… 1
   1. Motivation… 2
1. Survey 3
   1. Problem Definition 3
   1. Objectives 3
   1. Hardware and Software Requirement… 3
1. System Design… 4
   1. HTML/ CSS/ Python Connectivity… 4
   1. Data Flow Diagram… 4
   1. Deployment… 5
1. Implementation… 6
   1. Implementation Methods 6

4.1.1 Identification of Dataset 6

4.1.2 Choosing statistical measures 6

4.1.3 Using Flask to make a web application 7

1. Algorithms… 8
1. Results and Discussion… 9
1. Conclusion and Future Work 12

**References 13**

**_Appendix 14_**

# **List of Figures**

#

1. Figure 1 Data Flow diagram …4
1. Figure Pie Chart representing distribution of genres of movies in dataset …9
1. Figure 3 Number of movies released by different production companies ..10
1. Figure 4 Bar graph representing the data in movies_metadata.csv ..10
1. Figure 5 Bar graph displaying the genres of different movies in database …11
1. Figure 6 Graph representing the movie count of different directors …11
1. Figure 7 Input page of the web application …………………………………………….12
1. Figure 8 Movies recommended by the engine…………………………………………..12

## **CHAPTER 1**

## **INTRODUCTION**

![](/README/Aspose.Words.b3b2922a-bbea-468d-8499-819230b179f7.003.png)

1. **Overview**

` `A Movie recommendation system was developed for the purpose of recommending movies to user based on ratings by previous users and other parameters like cast, crew, keywords of the movie plots, etc. Recommendation system was developed over a span of three months in three different stages. The model proposed in this project is a hybrid recommendation system [4] which consists of features of both content based filtering [2] and collaborative based filtering [3]. In order to do so, statistical measures TF-IDF and cosine similarity have been used.

1. **The Goals**

The goal of this thesis project is to do the research of Recommendation Systems and find a suitable way to implement Movie Recommendation System for Project Based learning. There are many kinds of Recommender Systems but not all of them are suitable for one specific problem and situation.

1. ` `**Problem Statement**

` `We confront various challenges when creating a recommender system from the ground up. There are many recommender systems based on user information already available but What should we do if the website does not have enough users? Then we’ll figure out the representation of a movie, which is how a system can understand a movie. That is the precondition for comparing similarity between two movies. Movie parameters such as genre[2], actor, and director help to categorize films. However, each feature of the film should be given a distinct weight, and each one should play a different role for recommendation.

` `So, we get these questions:

- ` `How to recommend movies when there is no user information?
- ` `What kind of movie parameters can be used for the recommender system?
- ` `How to calculate the similarity between two movies?
- ` `Is it possible to set weight for each feature?

1. ` `**Motivation**

` `Over the past twenty years, there has been a rise in the use of recommender systems in various fields of e-commerce, music, finance, stock market, etc. With the inception of online streaming services, internet users have gained access to a large number of movies in the last few years at relatively low prices. As time is a valuable resource, there is a need for recommendation systems in order to save time for the users. This has led to companies like Amazon and Netflix [1] implementing different recommendation systems on their streaming platforms. This project proposes a hybrid recommendation system which uses features of both content based filtering and collaborative filtering in order to make accurate predictions.

## **CHAPTER 2**

## **SURVEY**

![](/README/Aspose.Words.b3b2922a-bbea-468d-8499-819230b179f7.003.png)

` `**2.1 Problem Definition**

To build a recommendation system which recommends similar movies based on ratings of previous users when a user enters an input into the search bar using the concepts of TF-IDF and cosine similarity.

` `**2.2 Objectives**

- To have a faster back-end source code than pure content-based filtering
- To make similar recommendations to the ones made by pure content-based filtering systems
- Creating a better dataset filtering system for better evaluation of the vectors.
- To have a highly stable and robust back end to create a website or an app for future expansions.

**2.3 Hardware and Software Requirements**
\*\*

` `**Software Requirement**

1. Language Used: Python, HTML, CSS
1. Technology: Python 3.10 and above
1. Source Code Editor: Visual Studio Code 1.67
1. Flask 2.1
1. Cloudflare 2022.5.0

**Hardware Requirement**

Hardware must be system of following configuration or above: -

1. Processor: Pentium G4560, 2 Cores 4 Threads, Processor band frequency: 3.50 GHz
1. Hard Disk: 1 TB
1. RAM: 8 GB, DDR4-2133Mhz@1.35V
1. Monitor, Keyboard, Mouse, UPS

## **CHAPTER 3**

## **SYSTEM DESIGN**

![](/README/Aspose.Words.b3b2922a-bbea-468d-8499-819230b179f7.003.png)

` `**3.1 HTML/CSS/PYTHON CONNECTIVITY**

In the project, we have used an index.html file which contains an inline CSS file. For the purpose of building the web application, the flask framework has been used. Flask is a micro web framework that was developed by Armin Ronacher.

` `**3.2 DATA FLOW DIAGRAM**

_Figure 1: Data flow diagram to represent the working of the recommendation model_

![](/README/Aspose.Words.b3b2922a-bbea-468d-8499-819230b179f7.004.png)![](Aspose.Words.b3b2922a-bbea-468d-8499-819230b179f7.005.png)

**3.3. Deployment**

Cloudflare has been used to host the website. Cloudflare functions as a reverse proxy between a website’s visitor and the Cloudflare customer’s hosting provider.

Cloudflare sets up a tunnel using localhost website link and requests Cloudflare through its CLI to request for an available domain name and allow to host websites over the world wide web.

## **CHAPTER 4 IMPLEMENTATION![](/README/Aspose.Words.b3b2922a-bbea-468d-8499-819230b179f7.006.png)**

**4.1 IMPLEMENTATION METHODS**

**4.1.1. Identification of Dataset**

The dataset identified for this project contains metadata for 45,000 movies along with 26 million ratings from 2,70,000 users for all 45,000 movies. The ratings are on the scale of 1-5. The data is used in the form of three CSV files: credits.csv, keywords.csv and movies_metadata.csv.

movies_metadata.csv : - It is the main metadata csv file. It contains information on the 45000 movies which includes information such as posters, backdrops, budget, revenue, release dates, languages, production countries and companies.

credits.csv : - It consists of cast and crew information for all movies.

keywords.csv : -It contains the movie plot keywords for the movies in the dataset.

**4.1.2. Choosing statistical measures**

The model proposed in this project is a hybrid recommendation system which consists of features of both content based filtering and collaborative based filtering. In order to do so, statistical measures TF-IDF and cosine similarity have been used.

**TF-IDF**

TF-IDF[9] is an abbreviation for Term Frequency - Inverse Document Frequency. It is a statistical measure used to quantify words in a set of documents. TF-IDF is often used as a weighting factor in searches of information retrieval, text mining, and user modeling. TF-IDF consists of term frequency (TF) and inverse document frequency (IDF). The TF-IDF scores are given by: -

**tf-idf(t, d) = tf(t, d). idf(t)**

where,
t = term(word)
d = document

To calculate term frequency, we divide the count of the term t in the document d by the total number of words in the document.

**tf(t,d) = count of t in d / number of words in d**

Inverse document frequency is the logarithmically scaled inverse of the fraction of documents that contain the term. It is calculated using the following formula: -

**idf(t) = log (N / (df + 1))**
\*\*

` `**Cosine Similarity**

It is the statistical measure [5] that is used to determine the similarity between two sequences of numbers. For calculating cosine similarity, the two sequences of numbers are viewed as vectors and cosine similarity is the cosine value of the angle between the two vectors.

cosθ= A.B|A| .|B|

**4.1.3 Using flask to make a web application**

For building the web application, the flask framework has been used. Flask[10] is a micro web framework that was developed by Armin Ronacher. We have route() decorator in flask to bind URL to a function. We are using GET and POST methods to send and receive data from our URL. For Creating the website, we have used HTML. The HTML file has been added to a folder called templates. Then the method render_template() is called to render the HTML file on browser.

**4.2 Algorithm**

**Step 1:** Start

**Step 2:** Read movies_metadata.csv and credits.csv files

**Step 3:** Find directors of movies

**Step 4:** Calculating the top movies in the dataset based on votes

**Step 5:** Merge the data from the two csv files into a single file

**Step 6:** Performing data cleaning and removing stop-words

**Step 7:** Generating tf-idf values for movies

**Step 8:** Finding cosine similarity based on tf-idf scores

**Step 9:** Displaying the recommendations

**Step 10:** Exit

## **CHAPTER 5 RESULTS AND DISCUSSION**

![](/README/Aspose.Words.b3b2922a-bbea-468d-8499-819230b179f7.003.png)

` `**Analysis of the dataset**

The dataset that was used for the project consists of metadata of 45000 movies. The following graphs and charts represent the different types of genres in the dataset, number of movies release by different production companies and the movie count of different directors.

![](/README/Aspose.Words.b3b2922a-bbea-468d-8499-819230b179f7.007.png)

_Figure 2 Pie chart representing distribution of genres of movies in the dataset_

![](/README/Aspose.Words.b3b2922a-bbea-468d-8499-819230b179f7.008.png)

_Figure 3 Number of movies released by different production companies_

![](/README/Aspose.Words.b3b2922a-bbea-468d-8499-819230b179f7.009.png)

_Figure 4 Bar graph representing the data in movies_metadata.csv_

![](/README/Aspose.Words.b3b2922a-bbea-468d-8499-819230b179f7.010.png)

_Figure 5 Bar graph displaying the genres of different movies in the database_

![](/README/Aspose.Words.b3b2922a-bbea-468d-8499-819230b179f7.011.png)

_Figure 6 Graph representing the movie count of different directors_

**Web Application**

A front end for the recommendation system has been created which displays the recommendations. The user enters an input (name of the movie) into the search bar which makes a query to the backend. The results of the recommendation are displayed on the web page.

![Graphical user interface, text, application

Description automatically generated](Aspose.Words.b3b2922a-bbea-468d-8499-819230b179f7.012.png)

_Figure 7 Input page of the web application_

![Text

Description automatically generated](Aspose.Words.b3b2922a-bbea-468d-8499-819230b179f7.013.png)

_Figure 8 Movies recommended by the engine_

## **CHAPTER 6 CONCLUSION AND FUTURE SCOPE![](/README/Aspose.Words.b3b2922a-bbea-468d-8499-819230b179f7.006.png)**

A hybrid movie recommendation system which uses features of both content based and collaborative based filtering systems has been identified. This hybrid model uses tf-idf to calculate weights of ratings given by previous users and makes use of cosine similarity to make predictions. Appropriate tests have been done for validation of results which are mentioned in the appendix of the report.

In the future, a recommendation system with a deep learning model [7][8] can be implemented.

## **REFERENCES**

[1] Gomez-Uribe, C.A. and Hunt, N., 2015. The netflix recommender system: Algorithms, business value, and innovation. *ACM Transactions on Management Information Systems (TMIS)*, *6*(4), pp.1-19.

[2] Reddy, S.R.S., Nalluri, S., Kunisetti, S., Ashok, S. and Venkatesh, B., 2019. Content-based movie recommendation system using genre correlation. In Smart Intelligent Computing and Applications (pp. 391-397). Springer, Singapore.

[3] Subramaniyaswamy, V., Logesh, R., Chandrashekhar, M., Challa, A. and Vijayakumar, V., 2017. A personalised movie recommendation system based on collaborative filtering. International Journal of High-Performance Computing and Networking, 10(1-2), pp.54-63.

[4] Dong, B., Zhu, Y., Li, L. and Wu, X., 2020. Hybrid collaborative recommendation via dual-autoencoder. IEEE Access, 8, pp.46030-46040.

[5] Rahutomo, F., Kitasuka, T. and Aritsugi, M., 2012, October. Semantic cosine similarity. In *The 7th International Student Conference on Advanced Science and Technology ICAST* (Vol. 4, No. 1, p. 1).

[6] Erdt, Mojisola, Alejandro Fernández, and Christoph Rensing. "Evaluating recommender systems for technology enhanced learning: a quantitative survey." IEEE Transactions on Learning Technologies 8.4 (2015): 326-344.

[7] Kaushik, A., Gupta, S. and Bhatia, M., 2018. A movie recommendation. System using Neural Networks. _International Journal of Advance Research, Ideas and Innovations in Technology_, _4_(2), pp.425-430.

[8] Furtado, F. and Singh, A., 2020. Movie recommendation system using machine learning. _International journal of research in industrial engineering_, _9_(1), pp.84-98.

[9] Ramos, J., 2003, December. Using tf-idf to determine word relevance in document queries. In *Proceedings of the first instructional conference on machine learning* (Vol. 242, No. 1, pp. 29-48).

[10] Grinberg, M., 2018. *Flask web development: developing web applications with python*. " O'Reilly Media, Inc.".APPENDIX

\*\*

**Validating the Recommendations:**

Recommender systems depend heavily on data. They provide trustworthy recommendations based on the data they have. A successful recommender system is one which is able to predict user’s choice accurately. Thus, we need to validate our recommendations using a few evaluation metrics [6] namely Root Mean Square Error (RMSE) and Mean Squared Error (MSE).

` `RMSE (root mean square error) gives us the difference between actual results and our calculated results from the recommendation system. It defines the quality of our recommendation system (which uses quantitative data), how accurate our recommendations system has predicted, or the percentage of error in our recommendation system. The larger the RMSE will be the inaccuracy of our recommendations and vice versa.

**RMSE=**1n i=1n(Yi - Yi)2

Where Yi represents the value predicted by Pearson Jaccard Similarity whereas Yi are the values predicted by the proposed model.

MSE (Mean squared error) gives us the squared difference between actual results and the results predicted by the recommendation system. It is always positive value which decreases as the error approaches zero. Thus, Larger MSE means our recommendations are more inaccurate.

**MSE=**1n i=1n(Yi - Yi)2

Where Yi represents the value predicted by Pearson Jaccard Similarity whereas Yi are the values predicted by the proposed model.

` `Validation of recommendations is achieved through comparing the recommendations of the proposed recommender system with recommendations generated using Pearson and Jaccard similarity scores.

The RMSE and MSE values between the similarity predicted using the proposed recommendation and the similarity scores predicted using Pearson and Jaccard are calculated. For movie: The Dark Knight, 0.00552 and 0.07429670248402684 were obtained as the MSE and RMSE values respectively. These MSE and RMSE values prove that the recommendations obtained are accurate.
