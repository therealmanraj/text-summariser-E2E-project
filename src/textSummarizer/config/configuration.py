from textSummarizer.constants import *
from textSummarizer.utils.common import read_yaml, create_directories
from textSummarizer.entity import (DataIngestionConfig,DataValidationConfig,DataTransformationConfig,ModelTrainingConfig,ModelEvaluationConfig)

class ConfigurationManager:
    def __init__(self, config_filepath = CONFIG_FILE_PATH, params_filepath = PARAMS_FILE_PATH):
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        
        create_directories([self.config.artifacts_root])
        
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion
        create_directories([config.root_dir])
        
        return DataIngestionConfig(
            root_dir=Path(self.config.data_ingestion.root_dir),
            source_URL=self.config.data_ingestion.source_URL,
            local_data_file=Path(self.config.data_ingestion.local_data_file),
            unzip_dir=Path(self.config.data_ingestion.unzip_dir)
        )
        
    def get_data_validation_config(self) -> DataValidationConfig:
        config = self.config.data_validation
        create_directories([config.root_dir])
        
        return DataValidationConfig(
            root_dir=Path(self.config.data_validation.root_dir),
            STATUS_FILE=self.config.data_validation.STATUS_FILE,
            ALL_REQUIRED_FILES=self.config.data_validation.ALL_REQUIRED_FILES
        )
        
    def get_data_transformation_config(self) -> DataTransformationConfig:
        config = self.config.data_transformation
        create_directories([config.root_dir])
        
        return DataTransformationConfig(
            root_dir=self.config.data_transformation.root_dir,
            DATA_PATH=self.config.data_transformation.DATA_PATH,
            TOKENIZER_NAME=Path(self.config.data_transformation.TOKENIZER_NAME)
        )
        
    def get_model_training_config(self) -> ModelTrainingConfig:
        config = self.config.model_training
        params = self.params.TrainingArguments

        create_directories([config.root_dir])

        model_training_config = ModelTrainingConfig(
            root_dir=config.root_dir,
            data_path=config.DATA_PATH,
            model_ckpt = config.MODEL_CKPT,
            num_train_epochs = params.num_train_epochs,
            warmup_steps = params.warmup_steps,
            per_device_train_batch_size = params.per_device_train_batch_size,
            weight_decay = params.weight_decay,
            logging_steps = params.logging_steps,
            evaluation_strategy = params.evaluation_strategy,
            eval_steps = params.eval_steps,
            save_steps = params.save_steps,
            gradient_accumulation_steps = params.gradient_accumulation_steps
        )

        return model_training_config
    
    def get_model_evaluation_config(self) -> ModelEvaluationConfig:
        config = self.config.model_evaluation
        create_directories([config.root_dir])
        model_evaluation_config = ModelEvaluationConfig(
            root_dir=config.root_dir,
            data_path=config.data_path,
            model_path = config.model_path,
            tokenizer_path = config.tokenizer_path,
            metric_file_name = config.metric_file_name
           
        )
        return model_evaluation_config