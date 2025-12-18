import logging
import logging.config
import config.paths as paths

logging.config.fileConfig(
    paths.LOGGER_CONFIG,
    defaults={"LOG_FILE": str(paths.LOG_FILE).replace("\\", "/")}
)

logger = logging.getLogger(__name__)