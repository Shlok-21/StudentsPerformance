# Predicting Student's Math Scores

## Overview
This repository contains code for building a machine learning model to predict students' math scores based on various features such as gender, race/ethnicity, parental level of education, lunch type, and test preparation course. The aim is to develop an accurate model that can assist in understanding factors influencing students' academic performance.

## Dataset
The dataset used for this project consists of the following columns:
- Gender
- Race/Ethnicity
- Parental Level of Education
- Lunch Type
- Test Preparation Course
- Math Score (target variable)
- Reading Score
- Writing Score

## Machine Learning Models Utilized
Several machine learning algorithms were explored to develop the predictive model. The models used include:
- Linear Regression
- Ridge Regression
- Lasso Regression
- Support Vector Regression (SVR)
- Decision Tree Regression
- Random Forest Regression
- K-Nearest Neighbors Regression
- Gradient Boosting Regression
- AdaBoost Regression
- CatBoost Regression
- XGBoost Regression

## Model Evaluation and Selection
To identify the best performing models, techniques such as Randomized Search Cross-Validation (RandomizedSearchCV) were employed to tune hyperparameters and optimize model performance. Model evaluation metrics such as mean squared error (MSE), root mean squared error (RMSE), and R-squared values were utilized to assess predictive accuracy and generalization capabilities.

## Final Model Selection
After thorough evaluation, the best-performing models were selected based on their predictive accuracy and performance metrics. These models were potentially combined or further fine-tuned to create the best final predictive model for estimating students' math scores based on the given features.

## Summary 
This project entails developing a comprehensive data processing and modeling pipeline utilizing Python, Flask, Docker, and AWS for deployment. Tasks include conducting thorough EDA, feature engineering, model training, website creation, Dockerization, CI/CD implementation, and AWS deployment setup. The objective is to deliver a robust, scalable solution for data analysis and predictive analytics.

## Project Structure
1. **Setup GitHub and Local Folder**
    * Create GitHub repo and .gitignore
    * Create venv
    * Create `setup.py`
    * Create `requirements.txt` 

2. **Create Source Code Structure**
    * Create `src` directory and build the package (`requirements.txt`)
        * Create component files: `data_ingestion.py`, `data_transformation.py`, `model_trainer.py`
        * Create pipeline files: `predict_pipeline.py`, `train_pipeline.py`
        * Create exception, logger, and utils files: `exceptions.py`, `logger.py`, `utils.py`

3. **Exploratory Data Analysis (EDA) in Jupyter Notebook**
    * Perform EDA
    * Handle missing values
    * Remove duplicate values
    * Data cleaning
    * Data imputation
    * Feature engineering
    * Train-test split
    * Identify best performing models
    * Model evaluation (R2)

4. **Create Simple Webpage for User Input**

5. **Write Modular Code with respect to the Jupyter Notebook and Test on Local Server (Flask)**

6. **Docker Configuration and Deployment**
    * Docker setup and configuration
    ```
    sudo apt-get update -y
    sudo apt-get upgrade

    curl -fsSL https://get.docker.com -o get-docker.sh

    sudo sh get-docker.sh

    sudo usermod -aG docker ubuntu

    newgrp docker
    ```
    * Build Docker image

7. **Configure GitHub Workflow and CI/CD Action Runner**

![image](https://github.com/Shlok-21/StudentsPerformance/assets/91182775/516902df-11bb-4f1c-a082-4ba15e1e7ad7)


8. **Setup AWS Resources for Deployment**

    * Create and configure IAM user
![image](https://github.com/Shlok-21/StudentsPerformance/assets/91182775/d9a88d6a-7a65-4ded-9c53-ef8f0d03f782)

    * Set up Amazon ECR repository
![image](https://github.com/Shlok-21/StudentsPerformance/assets/91182775/2d6a8cfb-1c29-4816-bdb7-710a700274d2)

    * Provision EC2 instance for deployment
![image](https://github.com/Shlok-21/StudentsPerformance/assets/91182775/fe508e29-c461-4197-aff8-faf77d128cfe)


## Final Result
![image](https://github.com/Shlok-21/StudentsPerformance/assets/91182775/1070550f-50cd-4ab1-9834-ac2954024545)

![image](https://github.com/Shlok-21/StudentsPerformance/assets/91182775/99254c10-4692-44c7-8e6d-76bcd0663713)
