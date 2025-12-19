from simpleoring.logging.logger import logger
logger.info("hi")

from simpleoring.mech import oring
x = oring.FaceSeal(usage="a")
print(x)