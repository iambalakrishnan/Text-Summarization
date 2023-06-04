from src.textSummarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline

from src.textSummarizer.logging.log import logger

STAGE_NAME ="Stage 01 - Data Ingestion "

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>> stage {STAGE_NAME} finished <<<<<< \n\n {120*'='}",)
except Exception as e:
    logger.exception(e)
    raise e