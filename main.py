from textSummarizer.pipeline.data_ingestion import DataIngestionTrainingPipeline
from textSummarizer.pipeline.data_validation import DataValidationTrainingPipeline
from textSummarizer.pipeline.data_transformation import DataTransformationTrainingPipeline
from textSummarizer.pipeline.model_training import ModelTrainingPipeline
from textSummarizer.pipeline.model_evaluation import ModelEvaluationPipeline
from textSummarizer.logging import logger

if __name__ == "__main__":
    
    try:
        logger.info(f"Starting data ingestion...")
        data_ingestion = DataIngestionTrainingPipeline()
        data_ingestion.main()
        logger.info(f"Data ingestion completed successfully.")
    except Exception as e:
        logger.error(f"An error occurred during data ingestion: {e}")
        raise e

    try:
        logger.info(f"Starting data validation...")
        data_validation = DataValidationTrainingPipeline()
        data_validation.main()
        logger.info(f"Data validation completed successfully.")
    except Exception as e:
        logger.error(f"An error occurred during data validation: {e}")
        raise e

    try:
        logger.info(f"Starting data transformation ...")
        data_transforamtion = DataTransformationTrainingPipeline()
        data_transforamtion.main()
        logger.info(f"Data transformation completed successfully.")
    except Exception as e:
        logger.error(f"An error occurred during data transformation: {e}")
        raise e

    try:
        logger.info(f"Starting model training...")
        model_training = ModelTrainingPipeline()
        model_training.main()
        logger.info(f"Model training completed successfully.")
    except Exception as e:
        logger.error(f"An error occurred during model training: {e}")
        raise e
    
    try:
        logger.info(f"Starting model evaluation...")
        model_evaluation = ModelEvaluationPipeline()
        model_evaluation.main()
        logger.info(f"Model evaluation completed successfully.")
    except Exception as e:
        logger.error(f"An error occurred during model evaluation: {e}")
        raise e
