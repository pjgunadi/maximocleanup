from psdi.util.logging import MXLogger
from psdi.util.logging import MXLoggerFactory
from psdi.mbo import MboConstants
from psdi.mbo import SqlFormat
from psdi.server import MXServer

print "CLEANUPWORKORDER - START"
#Log for debugging
logger = MXLoggerFactory.getLogger("maximo.script");
logger.debug("ScriptName" + launchPoint)

#PMCHGIAASSESMENT
pmchgiaassesmentSet = mbo.getMboSet("PMCHGIAASSESMENT")
if (not pmchgiaassesmentSet.isEmpty()):
    wonum = mbo.getString("WONUM")
    mxServer = MXServer.getMXServer()
    conKey = mxServer.getSystemUserInfo().getConnectionKey()
    con = mxServer.getDBManager().getConnection(conKey)
    try:
        preparedstmt = con.prepareStatement("delete pmchgiaassesment where wonum=?")
        preparedstmt.setString(1, wonum)
        iresult = preparedstmt.executeUpdate()
        if (iresult > 0):
            print "Deleted PMCHGIAASSESMENT wonum = " + wonum
        con.commit()
        con.close()
    except Exception,e:
        print e

#WOACTIVITY
woactivitySet = mbo.getMboSet("WOACTIVITY")
if (not woactivitySet.isEmpty()):
    i=0
    woactivityMbo = woactivitySet.getMbo(i)
    while (woactivityMbo is not None):
        #WOACTIVITY - CHILDREN
        wochildrenSet = woactivityMbo.getMboSet("CHILDREN")
        if (not wochildrenSet.isEmpty()):
            wochildrenSet.deleteAll(MboConstants.NOACCESSCHECK)

        #WOACTIVITY - WFINSTANCE
        strownertable = woactivityMbo.getString("WOCLASS")
        strownerid = woactivityMbo.getString("WORKORDERID")
        sqlf = SqlFormat("ownertable=:1 and ownerid=:2")
        sqlf.setObject(1, "WOACTIVITY","WOCLASS", strownertable)
        sqlf.setObject(2, "WOACTIVITY", "WORKORDERID", strownerid)
        wfinstanceSet = woactivityMbo.getMboSet("$wfinstance", "WFINSTANCE", sqlf.format())
        if (not wfinstanceSet.isEmpty()):
            wfinstanceSet.deleteAll(MboConstants.NOACCESSCHECK)

        #WOACTIVITY - WORKLOG
        worklogSet = woactivityMbo.getMboSet("MODIFYWORKLOG")
        if (not worklogSet.isEmpty()):
            worklogSet.deleteAll(MboConstants.NOACCESSCHECK)

        #WOACTIVITY - COMMLOG
        commlogSet = woactivityMbo.getMboSet("COMMLOG")
        if (not commlogSet.isEmpty()):
            commlogSet.deleteAll(MboConstants.NOACCESSCHECK)

        #WOACTIVITY - WORKORDERSPEC
        wospecSet = woactivityMbo.getMboSet("WORKORDERSPEC")
        if (not wospecSet.isEmpty()):
            wospecSet.deleteAll(MboConstants.NOACCESSCHECK)

        #RELATEDRECORD
        relatedrecordSet = woactivityMbo.getMboSet("RELATEDRECORD")
        if (not relatedrecordSet.isEmpty()):
            relatedrecordSet.deleteAll(MboConstants.NOACCESSCHECK)
        woactivityMbo.setValueNull('CLASSSTRUCTUREID', MboConstants.NOACCESSCHECK + MboConstants.NOVALIDATION_AND_NOACTION)
        i += 1
        woactivityMbo = woactivitySet.getMbo(i)
    #DELETEWOACTIVITY
    woactivitySet.deleteAll(MboConstants.NOACCESSCHECK)

#WFINSTANCE
strownertable = mbo.getString("WOCLASS")
strownerid = mbo.getString("WORKORDERID")
sqlf = SqlFormat("ownertable=:1 and ownerid=:2")
sqlf.setObject(1, "WOCHANGE","WOCLASS", strownertable)
sqlf.setObject(2, "WOCHANGE", "WORKORDERID", strownerid)
wfinstanceSet = mbo.getMboSet("$wfinstance", "WFINSTANCE", sqlf.format())
#wfinstanceMbo = commTemplateSet.getMbo(0)
if (not wfinstanceSet.isEmpty()):
    wfinstanceSet.deleteAll(MboConstants.NOACCESSCHECK)

#WORKLOG
worklogSet = mbo.getMboSet("MODIFYWORKLOG")
if (not worklogSet.isEmpty()):
    worklogSet.deleteAll(MboConstants.NOACCESSCHECK)

#COMMLOG
commlogSet = mbo.getMboSet("COMMLOG")
if (not commlogSet.isEmpty()):
    commlogSet.deleteAll(MboConstants.NOACCESSCHECK)

#WORKORDERSPEC
wospecSet = mbo.getMboSet("WORKORDERSPEC")
if (not wospecSet.isEmpty()):
    wospecSet.deleteAll(MboConstants.NOACCESSCHECK)

#RELATEDRECORD
relatedrecordSet = mbo.getMboSet("RELATEDRECORD")
if (not relatedrecordSet.isEmpty()):
    relatedrecordSet.deleteAll(MboConstants.NOACCESSCHECK)

#DELETEMBO
mbo.setValueNull('CLASSSTRUCTUREID', MboConstants.NOACCESSCHECK + MboConstants.NOVALIDATION_AND_NOACTION)
mbo.delete(MboConstants.NOACCESSCHECK)

print "CLEANUPWORKORDER - END"
