from src.core.config import get_Settings
from src.core.logger import get_logger

settings = get_Settings()
logger = get_logger(__name__)

logger.info(f"App environment: {settings.APP_ENV}")
logger.info(f"Neo4j URI: {settings.NEO4J_URI}")
logger.info(f"Groq key loaded: {bool(settings.GROQ_API_KEY)}")