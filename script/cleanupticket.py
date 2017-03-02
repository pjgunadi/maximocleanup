from psdi.util.logging import MXLogger
from psdi.util.logging import MXLoggerFactory
from psdi.mbo import MboConstants
from psdi.mbo import SqlFormat

print "CLEANUPTICKET - START"
#Log for debugging
logger = MXLoggerFactory.getLogger("maximo.script");
logger.debug("ScriptName" + launchPoint)

#WFINSTANCE
strownertable = mbo.getString("CLASS")
strownerid = mbo.getString("TICKETUID")
sqlf = SqlFormat("ownertable=:1 and ownerid=:2")
sqlf.setObject(1, "TICKET","CLASS", strownertable)
sqlf.setObject(2, "TICKET", "TICKETUID", strownerid)
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

#TICKETSPEC
ticketspecSet = mbo.getMboSet("TICKETSPEC")
if (not ticketspecSet.isEmpty()):
    ticketspecSet.deleteAll(MboConstants.NOACCESSCHECK)

#PERSISTSTATUS
persiststatusSet = mbo.getMboSet("PERSISTSTATUS")
if (not persiststatusSet.isEmpty()):
    persiststatusSet.deleteAll(MboConstants.NOACCESSCHECK)

#PLUSPTKPRICETOTALS
plustkpricetotalsSet = mbo.getMboSet("PLUSPTKPRICETOTALS")
if (not plustkpricetotalsSet.isEmpty()):
    plustkpricetotalsSet.deleteAll(MboConstants.NOACCESSCHECK)

strclass = mbo.getString("CLASS")
if (strclass == 'SR'):
    #PMSCCRSPEC
    #pmsccrspecSet = mbo.getMboSet("PMSCCRSPEC")
    strticketid = mbo.getString("TICKETID")
    strclassstructureid = mbo.getString("CLASSSTRUCTUREID")
    sqlf = SqlFormat("ticketid=:1 and classstructureid=:2")
    sqlf.setObject(1, "TICKET","TICKETID", strticketid)
    sqlf.setObject(2, "TICKET", "CLASSSTRUCTUREID", strclassstructureid)
    pmsccrspecSet = mbo.getMboSet("$pmsccrspec", "PMSCCRSPECV", sqlf.format())
    if (not pmsccrspecSet.isEmpty()):
        pmsccrspecSet.deleteAll(MboConstants.NOACCESSCHECK)

    #PMSCCR
    #pmsccrSet = mbo.getMboSet("PMSCCR")
    strpmsccrid = mbo.getString("PMSCCRID")
    sqlf = SqlFormat("pmsccrnum=:1")
    sqlf.setObject(1, "TICKET","PMSCCRID", strpmsccrid)
    pmsccrSet = mbo.getMboSet("$pmsccr", "PMSCCR", sqlf.format())
    if (not pmsccrSet.isEmpty()):
        i=0
        pmsccrMbo = pmsccrSet.getMbo(i)
        while (pmsccrMbo is not None):
            #PMSCCR - PMSCCRSTATUS
            pmsccrstatusSet = pmsccrMbo.getMboSet("PMSCCRSTATUS")
            if (not pmsccrstatusSet.isEmpty()):
                pmsccrstatusSet.deleteAll(MboConstants.NOACCESSCHECK)
            i += 1
            pmsccrMbo = pmsccrSet.getMbo(i)
        #DELETEALL PMSCCR
        pmsccrSet.deleteAll(MboConstants.NOACCESSCHECK)

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


#RELATEDRECORD
relatedrecordSet = mbo.getMboSet("RELATEDRECORD")
if (not relatedrecordSet.isEmpty()):
    relatedrecordSet.deleteAll(MboConstants.NOACCESSCHECK)

#DELETEMBO
mbo.setValueNull('CLASSSTRUCTUREID', MboConstants.NOACCESSCHECK + MboConstants.NOVALIDATION_AND_NOACTION)
mbo.delete(MboConstants.NOACCESSCHECK)

print "CLEANUPTICKET - END"
