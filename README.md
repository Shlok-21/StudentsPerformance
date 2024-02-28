
## Summary 
This project entails developing a comprehensive data processing and modeling pipeline utilizing Python, Flask, Docker, and AWS for deployment. Tasks include conducting thorough EDA, feature engineering, model training, website creation, Dockerization, CI/CD implementation, and AWS deployment setup. The objective is to deliver a robust, scalable solution for data analysis and predictive analytics.

## Project Structure
---
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

5. **Write Modular Code with Respect to the Jupyter Notebook and Test on Local Server (Flask)**

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
---
![image](https://github.com/Shlok-21/StudentsPerformance/assets/91182775/1070550f-50cd-4ab1-9834-ac2954024545)

![image](https://github.com/Shlok-21/StudentsPerformance/assets/91182775/99254c10-4692-44c7-8e6d-76bcd0663713)
