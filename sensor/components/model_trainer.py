import os, sys
from sensor.exception import SensorException
from sensor.logger import logging
from sensor.entity.artifact_entity import DataTransformationArtifact, ModelTrainerArtifact
from sensor.entity.config_entity import ModelTrainerConfig
from sensor.utils.main_utils import load_numpy_array_data, save_object, load_object
from sensor.ml.model.estimator import SensorModel
from sensor.ml.metric.classification_metric import get_classification_score
from xgboost import XGBClassifier


class ModelTrainer:

    def __init__(self, 
                 model_trainer_config: ModelTrainerConfig,
                 data_transformation_artifact: DataTransformationArtifact):
        try:
            self.model_trainer_config = model_trainer_config
            self.data_transformation_artifact = data_transformation_artifact
        except Exception as e:
            raise SensorException(e, sys)

    def perform_hyper_parameter_tuning(self):
        """ Implement hyperparameter tuning here if needed """
        pass

    def train_model(self, x_train, y_train):
        """Train XGBoost classifier"""
        try:
            xgb_clf = XGBClassifier()
            xgb_clf.fit(x_train, y_train)
            return xgb_clf
        except Exception as e:
            raise SensorException(e, sys)

    def initiate_model_trainer(self) -> ModelTrainerArtifact:
        try:
            # ------------------------------
            # Load transformed train and test arrays
            # ------------------------------
            train_arr = load_numpy_array_data(self.data_transformation_artifact.transformed_train_file_path)
            test_arr = load_numpy_array_data(self.data_transformation_artifact.transformed_test_file_path)

            x_train, y_train = train_arr[:, :-1], train_arr[:, -1]
            x_test, y_test = test_arr[:, :-1], test_arr[:, -1]

            # ------------------------------
            # Train the model
            # ------------------------------
            model = self.train_model(x_train, y_train)

            # ------------------------------
            # Evaluate model
            # ------------------------------
            y_train_pred = model.predict(x_train)
            y_test_pred = model.predict(x_test)

            train_metric = get_classification_score(y_true=y_train, y_pred=y_train_pred)
            test_metric = get_classification_score(y_true=y_test, y_pred=y_test_pred)

            # Check accuracy threshold
            if train_metric.f1_score <= self.model_trainer_config.expected_accuracy:
                raise Exception("Trained model did not meet expected accuracy.")

            # Check overfitting/underfitting
            diff = abs(train_metric.f1_score - test_metric.f1_score)
            if diff > self.model_trainer_config.overfitting_underfitting_threshold:
                raise Exception("Model may be overfitting or underfitting. Try tuning hyperparameters.")

            # ------------------------------
            # Load preprocessor from DataTransformation artifact
            # ------------------------------
            preprocessor = load_object(file_path=self.data_transformation_artifact.transformed_object_file_path)

            # ------------------------------
            # Save model and preprocessor in SAVE_MODEL folder
            # ------------------------------
            save_model_dir = os.path.join(os.getcwd(), "save_model")  # separate folder in project root
            os.makedirs(save_model_dir, exist_ok=True)

            # Save preprocessing.pkl
            preprocessing_file_path = os.path.join(save_model_dir, "preprocessing.pkl")
            save_object(file_path=preprocessing_file_path, obj=preprocessor)
            logging.info(f"Preprocessing object saved at: {preprocessing_file_path}")

            # Save model.pkl
            model_file_path = os.path.join(save_model_dir, "model.pkl")
            save_object(file_path=model_file_path, obj=model)
            logging.info(f"Model object saved at: {model_file_path}")

            # Optional: Save SensorModel wrapper (model + preprocessor)
            sensor_model_file_path = os.path.join(save_model_dir, "sensor_model.pkl")
            sensor_model = SensorModel(preprocessor=preprocessor, model=model)
            save_object(file_path=sensor_model_file_path, obj=sensor_model)
            logging.info(f"SensorModel saved at: {sensor_model_file_path}")

            # ------------------------------
            # Return ModelTrainerArtifact
            # ------------------------------
            model_trainer_artifact = ModelTrainerArtifact(
                trained_model_file_path=sensor_model_file_path,
                train_metric_artifact=train_metric,
                test_metric_artifact=test_metric
            )
            logging.info(f"ModelTrainerArtifact: {model_trainer_artifact}")
            return model_trainer_artifact

        except Exception as e:
            raise SensorException(e, sys)

