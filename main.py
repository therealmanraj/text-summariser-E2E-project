from textSummarizer.pipeline.data_ingestion import DataIngestionTrainingPipeline
from textSummarizer.pipeline.data_validation import DataValidationTrainingPipeline
from textSummarizer.logging import logger

try:
    logger.info(f"Starting data ingestion pipeline...")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f"Data ingestion pipeline completed successfully.")
except Exception as e:
    logger.error(f"An error occurred during data ingestion pipeline: {e}")
    raise e

try:
    logger.info(f"Starting data validation pipeline...")
    data_validation = DataValidationTrainingPipeline()
    data_validation.main()
    logger.info(f"Data validation pipeline completed successfully.")
except Exception as e:
    logger.error(f"An error occurred during data validation pipeline: {e}")
    raise e