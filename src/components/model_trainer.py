import os
import sys

from dataclasses import dataclass

from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsRegressor
from sklearn.ensemble import AdaBoostRegressor, RandomForestRegressor, GradientBoostingRegressor
from catboost import CatBoostRegressor
from xgboost import XGBRegressor
from sklearn.tree import DecisionTreeRegressor

from sklearn.metrics import r2_score

from src.logger import logging 
from src.exception import CustomException
from src.utils import save_object, evaluate_model



@dataclass
class ModelTrainerConfig:
    trained_model_file_path = os.path.join('artifacts','model.pkl')

class ModelTrainer:
    def __init__(self):
        self.mdoel_trainer_config = ModelTrainerConfig()

    def initiate_model_trainer(self,train_array, test_array):
        try:
            logging.info('Splitting training and testing data')
            X_train, y_train, X_test, y_test = (
                train_array[:,:-1],
                train_array[:,-1],
                test_array[:,:-1],
                test_array[:,-1]
            )

            models = {
                'Random Forest': RandomForestRegressor(),
                'Decision Tree': DecisionTreeRegressor(),
                'Gradient Boosting': GradientBoostingRegressor(),
                'Linear Regression' : LinearRegression(),
                'KNeighbors Classifier' : KNeighborsRegressor(),
                'XGBClassifier' : XGBRegressor(),
                'CatBoosting Classifier' : CatBoostRegressor(),
                'Adaboost Classifier': AdaBoostRegressor()
            }

            model_report: dict= evaluate_model(X_train = X_train, y_train = y_train,X_test = X_test, y_test = y_test,
                                                models = models)
            
            best_model_score = max(sorted(model_report.values()))
            best_model_name = list(model_report.keys())[
                list(model_report.values()).index(best_model_score)
            ]

            best_model = models[best_model_name]

            if best_model_score <= 0.6:
                raise CustomException('No best model found')
            
            logging.info('Best model found on training and test data')

            save_object(
                file_path=ModelTrainerConfig.trained_model_file_path,
                obj = best_model
            )

            predicted = best_model.predict(X_test)
            r2_sc = r2_score(y_test, predicted)
            return r2_sc

        except Exception as e:
            raise CustomException(e,sys)
