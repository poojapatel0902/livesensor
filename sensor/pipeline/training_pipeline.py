<<<<<<< HEAD
import sys
from sensor.exception import SensorException
from sensor.logger import logging
from sensor.entity.config_entity import (TrainingPipelineConfig, DataIngestionConfig, DataValidationConfig, DataTransformationConfig, ModelTrainerConfig, ModelEvaluationConfig, ModelPusherConfig)
from sensor.entity.artifact_entity import (DataIngestionArtifact, DataValidationArtifact, DataTransformationArtifact, ModelTrainerArtifact, ModelEvaluationArtifact, ModelPusherArtifact)
from sensor.components.data_ingestion import DataIngestion
from sensor.components.data_validation import DataValidation
from sensor.components.data_transformation import DataTransformation
from sensor.components.model_trainer import ModelTrainer
from sensor.components.model_evaluation import ModelEvaluation
from sensor.components.model_pusher import ModelPusher

class TrainPipeline:
    def __init__(self):
        self.training_pipeline_config = TrainingPipelineConfig()
        
        # --- THE FIX: We are adding this flag directly ---
        self.is_pipeline_running = False

    def start_data_ingestion(self) -> DataIngestionArtifact:
        try:
            logging.info("Starting data ingestion")
            data_ingestion_config = DataIngestionConfig(training_pipeline_config=self.training_pipeline_config)
            data_ingestion = DataIngestion(data_ingestion_config=data_ingestion_config)
            return data_ingestion.initiate_data_ingestion()
        except Exception as e:
            raise SensorException(e, sys)

    def start_data_validation(self, data_ingestion_artifact: DataIngestionArtifact) -> DataValidationArtifact:
        try:
            data_validation_config = DataValidationConfig(training_pipeline_config=self.training_pipeline_config)
            data_validation = DataValidation(data_ingestion_artifact=data_ingestion_artifact, data_validation_config=data_validation_config)
            return data_validation.initiate_data_validation()
        except Exception as e:
            raise SensorException(e, sys)

    def start_data_transformation(self, data_validation_artifact: DataValidationArtifact) -> DataTransformationArtifact:
        try:
            data_transformation_config = DataTransformationConfig(training_pipeline_config=self.training_pipeline_config)
            data_transformation = DataTransformation(data_validation_artifact=data_validation_artifact, data_transformation_config=data_transformation_config)
            return data_transformation.initiate_data_transformation()
        except Exception as e:
            raise SensorException(e, sys)

    def start_model_trainer(self, data_transformation_artifact: DataTransformationArtifact) -> ModelTrainerArtifact:
        try:
            model_trainer_config = ModelTrainerConfig(training_pipeline_config=self.training_pipeline_config)
            model_trainer = ModelTrainer(model_trainer_config=model_trainer_config, data_transformation_artifact=data_transformation_artifact)
            return model_trainer.initiate_model_trainer()
        except Exception as e:
            raise SensorException(e, sys)

    def start_model_evaluation(self, data_validation_artifact: DataValidationArtifact, model_trainer_artifact: ModelTrainerArtifact) -> ModelEvaluationArtifact:
        try:
            model_evaluation_config = ModelEvaluationConfig(training_pipeline_config=self.training_pipeline_config)
            model_evaluation = ModelEvaluation(model_eval_config=model_evaluation_config, data_validation_artifact=data_validation_artifact, model_trainer_artifact=model_trainer_artifact)
            return model_evaluation.initiate_model_evaluation()
        except Exception as e:
            raise SensorException(e, sys)

    def start_model_pusher(self, model_eval_artifact: ModelEvaluationArtifact, data_transformation_artifact: DataTransformationArtifact) -> ModelPusherArtifact:
        try:
            model_pusher_config = ModelPusherConfig(training_pipeline_config=self.training_pipeline_config)
            model_pusher = ModelPusher(model_pusher_config=model_pusher_config, model_eval_artifact=model_eval_artifact, data_transformation_artifact=data_transformation_artifact)
            return model_pusher.initiate_model_pusher()
        except Exception as e:
            raise SensorException(e, sys)

    def run_pipeline(self):
        try:
            logging.info("Running Pipeline")
            self.is_pipeline_running = True

            data_ingestion_artifact = self.start_data_ingestion()
            data_validation_artifact = self.start_data_validation(data_ingestion_artifact=data_ingestion_artifact)
            data_transformation_artifact = self.start_data_transformation(data_validation_artifact=data_validation_artifact)
            model_trainer_artifact = self.start_model_trainer(data_transformation_artifact=data_transformation_artifact)
            model_eval_artifact = self.start_model_evaluation(data_validation_artifact=data_validation_artifact, model_trainer_artifact=model_trainer_artifact)

            if not model_eval_artifact.is_model_accepted:
                logging.info("Model not accepted.")
                self.is_pipeline_running = False
                return None

            model_pusher_artifact = self.start_model_pusher(
                model_eval_artifact=model_eval_artifact, 
                data_transformation_artifact=data_transformation_artifact
            )
            
            logging.info("Pipeline Completed Successfully.")
            self.is_pipeline_running = False

        except Exception as e:
            self.is_pipeline_running = False
            raise SensorException(e, sys)
=======
from sensor.entity.config_entity import TrainingPipelineConfig ,DataIngestionConfig
from sensor.exception  import SensorException
from sensor.entity.artifact_entity import DataIngestionArtifact
from sensor.logger import logging
import sys , os 
from sensor.components.data_ingestion import DataIngestion


from sensor.components.data_validation import DataValidation

from sensor.entity.config_entity import TrainingPipelineConfig,DataIngestionConfig,DataValidationConfig

from sensor.entity.artifact_entity import DataIngestionArtifact, DataValidationArtifact




class TrainPipeline:

    def __init__(self):
        self.training_pipeline_config = TrainingPipelineConfig()


    def start_data_ingestion(self)->DataIngestionArtifact:
        try:
            
            self.data_ingestion_config = DataIngestionConfig(training_pipeline_config=self.training_pipeline_config)

            logging.info("Starting data ingestion")

            data_ingestion = DataIngestion(data_ingestion_config=self.data_ingestion_config)

            data_ingestion_artifact = data_ingestion.initiate_data_ingestion()

            logging.info(f"Data ingestion completed and artifact: {data_ingestion_artifact}")
            return data_ingestion_artifact
        except  Exception as e:
            raise  SensorException(e,sys)







    def start_data_validaton(self,data_ingestion_artifact:DataIngestionArtifact)->DataValidationArtifact:
        
        try:
            data_validation_config = DataValidationConfig(training_pipeline_config=self.training_pipeline_config)

            data_validation = DataValidation(data_ingestion_artifact=data_ingestion_artifact,
            data_validation_config = data_validation_config
            )

            data_validation_artifact = data_validation.initiate_data_validation()

            return data_validation_artifact
        
        except  Exception as e:
            raise  SensorException(e,sys)









    def run_pipeline(self):
        try:
            
            data_ingestion_artifact:DataIngestionArtifact = self.start_data_ingestion()




            data_validation_artifact=self.start_data_validaton(data_ingestion_artifact=data_ingestion_artifact)

            
        except Exception as e :    
            raise  SensorException(e,sys)
>>>>>>> 3d86508f95b2fa2e912653e71d170582ed447b80
