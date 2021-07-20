![happyflyers](img/happyflyers.JPG)

Monash Data Bootcamp Final Project

The purpose of this project was to utilise Machine Learning models in order to analyse airline customers satisfaction data and deploy it to a HTML page.

# Data

There are two key sources of data used:

* [airlines-customer-satisfaction](https://www.kaggle.com/sjleshrac/airlines-customer-satisfaction) - kaggle dataset used for analysis with data from non-disclosed airline organization, which consists of the details of customers, feedback of the customers on various context and their flight data.

* [airlines-customer-income](https://data.worldbank.org/indicator/IS.AIR.PSGR) - worldbank dataset with airline customers income data used for main page chart.


# Analysis

## Data Cleaning - Jupyter Notebook

* Drop rows with Nan and 0 values

* Select relevant columns

## Machine Learning Models - Jupyter Notebook

* Load and pre-process data

* Create and train Random Forrest model to make overall customer prediction

* Save Random Forrest model to .pkl file

* Create and train four Logistic Regression models to make predictions for each customer profile

* Save results to csv files


## Flask Application

* Use Flask to create a HTML page that displays data and connects to the Machine Learning model to make predictions:

  * Create a root route `/` that will load template HTML file `index.html` 

  * Create a route called `/index_predict` that will open Random Forest model .pkl file, pass it data from the webpage and return prediction

  * Create routes called `/index_customerX` which display actual and predicted numbers of satisfied/non-satisfied customers for selected customer profile


## Webpage - HTML, CSS, JS, embedded Tableau and Flourish

* Create frontend using Bootstrap

* Add embedded Tableau dashboard

* Add input drowpdowns for Machine Learning model

* Create interactive charts using Flourish


## Webpage Deployment - Heroku

* Set up Heroku server and deploy the webpage through Github


# Demo

To see the Airline Satisfaction Report webpage visit https://happyflyers123.herokuapp.com/.


# Used Tools
 * Jupyter Notebook 
 * Pandas
 * Python
 * Flask
 * scikit-learn
 * Tableau
 * Flourish
 * JS
 * HTML
 * CSS
 * Heroku

