import sys
import os
import shutil
from sensor.exception import SensorException
from sensor.logger import logging
from sensor.entity.artifact_entity import ModelPusherArtifact, ModelEvaluationArtifact, DataTransformationArtifact
from sensor.entity.config_entity import ModelPusherConfig

class ModelPusher:
    def __init__(self, model_pusher_config: ModelPusherConfig,
                 model_eval_artifact: ModelEvaluationArtifact,
                 data_transformation_artifact: DataTransformationArtifact):
        try:
            self.model_pusher_config = model_pusher_config
            self.model_eval_artifact = model_eval_artifact
            self.data_transformation_artifact = data_transformation_artifact
        except Exception as e:
            raise SensorException(e, sys)

    def initiate_model_pusher(self) -> ModelPusherArtifact:
        try:
            # 1. Source Paths (Where the files are now)
            trained_model_path = self.model_eval_artifact.trained_model_path
            transformed_object_path = self.data_transformation_artifact.transformed_object_file_path

            # 2. Destination Paths (Where we want them to go -> saved_models)
            model_file_path = self.model_pusher_config.model_file_path
            
            # Create the folder (e.g., saved_models/timestamp/)
            os.makedirs(os.path.dirname(model_file_path), exist_ok=True)
            
            # Define name for preprocessor in saved_models
            # We save it next to the model file
            saved_model_directory = os.path.dirname(model_file_path)
            preprocessor_file_path = os.path.join(saved_model_directory, "preprocessing.pkl")

            logging.info(f"Saving model to: {model_file_path}")
            logging.info(f"Saving preprocessor to: {preprocessor_file_path}")

            # 3. Copy the files
            shutil.copy(trained_model_path, model_file_path)
            shutil.copy(transformed_object_path, preprocessor_file_path)

            # 4. Return Artifact
            model_pusher_artifact = ModelPusherArtifact(
                saved_model_path=model_file_path,
                model_file_path=model_file_path
            )
            return model_pusher_artifact

        except Exception as e:
            raise SensorException(e, sys)
