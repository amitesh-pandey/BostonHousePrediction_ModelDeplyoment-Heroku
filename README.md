# BostonHousePrediction_ModelDeplyoment-Heroku

This repository mainly focuses on creating a working Machine Learning model to predict the Pricing of the houses in Boston using Python as a coding language, Flask as a micro web framework and finally productionize the product on to the Heroku Platform.

This project is divided in to three main section : <br>
1. Creating a ML model which predicts the price of house based on the independent features <br>
2. Creating a flask web based micro framework <br>
3. Deplyoment of the model on to the Heroku Framework <br>

************************************************
Section 1 : Creating a ML based model: 
Boston House prediction dataset has been loaded from the sklearn dataset folder with the following commands as mentioned below

from sklearn.datasets import load_boston
boston = load_boston()
bos = pd.DataFrame(boston.data)

Model is been trained using Linear Regression based Supervised Machine Learning algorithm . The mse rates are calculated accordingly . Model is saved using pickle library and named as final_model.pkl

***********************************************
Section 2: Creating a flask web based micro framework :

Creating a new python file named as main.py, where the app is executed on to the following route (path) with two html files . Index.html is used to take the input from the web user and results need to be displayed on to the next web page name submit.html.

Screenshots of results are mentioned below for your reference : 

![1](https://user-images.githubusercontent.com/63364350/128605549-ce47b22d-1254-49d5-af2d-f15bf73d2f1b.PNG)
![2](https://user-images.githubusercontent.com/63364350/128605555-f3af6e82-c52d-4493-b0a2-bcfd02125c18.PNG)

************************************************
Section 3: Deplyoment of the model on to the Heroku Framework

There are two main things needed when using Heroku from Deployment :
1. Creating an account in heroku cloud . https://id.heroku.com/login
2. install gunicorn using pip commands and create a file name Procfile with the codes as mentioned in repository 
       !pip install gunicorn
3. Manually create the requirements.txt files which helps heroku server to create an environment in cloud with the necessary libraries installed 

Deploy in the Heroku is successfully achieved 
![image](https://user-images.githubusercontent.com/63364350/128606034-638d7c44-d526-401e-a0ea-f22bf014580d.png)

Below is the heroku link for your reference 

https://boston-house-prediction.herokuapp.com/

Enjoy Learning !!! 
