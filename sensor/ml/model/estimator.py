import os
from sensor.constant.training_pipeline import SAVED_MODEL_DIR, MODEL_FILE_NAME

class TargetValueMapping:
    def __init__(self):
        self.mapping = {
            "neg": 0,
            "pos": 1
        }

    def to_dict(self):
        return self.mapping

    def reverse_mapping(self):
        mapping_response = self.to_dict()
        return dict(zip(mapping_response.values(), mapping_response.keys()))

class SensorModel:
    def __init__(self, preprocessor, model):
        try:
            self.preprocessor = preprocessor
            self.model = model
        except Exception as e:
            raise e
    
    def predict(self, x):
        try:
            x_transform = self.preprocessor.transform(x)
            y_hat = self.model.predict(x_transform)
            return y_hat
        except Exception as e:
            raise e

class ModelResolver: 
    def __init__(self, model_dir=SAVED_MODEL_DIR):
        try:
            self.model_dir = model_dir
        except Exception as e:
            raise e    

    def get_best_model_path(self) -> str:
        try:
            # FIX: Check if folder exists first!
            if not os.path.exists(self.model_dir):
                return None

            dir_names = os.listdir(self.model_dir)
            timestamps = [int(dir_name) for dir_name in dir_names if dir_name.isdigit()]
    
            if len(timestamps) == 0:
                return None
        
            latest_timestamp = max(timestamps)
            latest_dir_path = os.path.join(self.model_dir, f"{latest_timestamp}", MODEL_FILE_NAME)
            
            return latest_dir_path
        except Exception as e:
            raise e 

    def is_model_exists(self) -> bool:
        try:
            if not os.path.exists(self.model_dir):
                return False

            timestamps = os.listdir(self.model_dir)
            if len(timestamps) == 0:
                return False
            
            latest_model_path = self.get_best_model_path()
            
            if latest_model_path is None:
                return False

            if not os.path.exists(latest_model_path):
                return False

            return True
        except Exception as e:
            raise e
        
    def get_best_preprocessing_object_path(self):
        try:
            # FIX: Check if folder exists first!
            if not os.path.exists(self.model_dir):
                return None

            dir_names = os.listdir(self.model_dir)
            timestamps = [int(dir_name) for dir_name in dir_names if dir_name.isdigit()]
            
            if len(timestamps) == 0:
                return None
            
            latest_timestamp = max(timestamps)
            latest_preprocessor_path = os.path.join(self.model_dir, f"{latest_timestamp}", "preprocessing.pkl")
            
            return latest_preprocessor_path
        except Exception as e:
            raise e