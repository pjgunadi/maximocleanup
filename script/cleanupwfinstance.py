from psdi.util.logging import MXLogger
from psdi.util.logging import MXLoggerFactory
from psdi.mbo import MboConstants

print "CLEANUPWFINSTANCE - START"
#Log for debugging
logger = MXLoggerFactory.getLogger("maximo.script");
logger.debug("ScriptName" + launchPoint)
mbo.delete(MboConstants.NOACCESSCHECK)

print "CLEANUPWFINSTANCE - END"
