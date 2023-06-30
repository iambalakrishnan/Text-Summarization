from src.textSummarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.textSummarizer.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from src.textSummarizer.logging.log import logger


#Data ingestion training pipeline
STAGE_NAME ="Stage 01 - Data Ingestion "

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>> stage {STAGE_NAME} finished <<<<<< \n\n {120*'='}",)
except Exception as e:
    logger.exception(e)
    raise e


#data validation pipeline

STAGE_NAME ="Stage 02 - Data Validation "

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    data_validation = DataValidationTrainingPipeline()
    data_validation.main()
    logger.info(f">>>>>> stage {STAGE_NAME} finished <<<<<< \n\n {120*'='}",)
except Exception as e:
    logger.exception(e)
    raise e