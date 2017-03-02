# Maximo Cleanup
IBM Maximo automation scripts (Jython) to cleanup MBOs such as Work Order, Ticket, and Asset

#Disclaimer
The script and steps are provided as is and use it at own risk. It is not recommended for production environment, please use maximo archiving product instead.

# Background
Certain maximo MBOs do not allow deletion after activities have been committed to the record such as change of status, applied workflow, and communication log
This behaviour could be expected in production environment. However, at some development and test environment, maximo designer may need to delete records after test activities.
This library has some script that may help the record deletion without needing to reinstall new maximo.

#Prepare Cleanup for Communication Log
##1. Create Script with Action Launch Point:
- Launch Point: CLEANUPCOMMLOG
- Description: Cleanup Communication Log
- Object: COMMLOG
- Action: CLEANUPCOMMLOG
- Action Description: Cleanup Communication Log
- Active: Ticked
- Script: New

###Continue with the next dialog for New Script Details:
- Script: CLEANUPGENERIC
- Script Description: Generic Cleanup Script
- Script Language: jython
- Source Code: import or copy the script from [cleanupgeneric.py](https://github.ibm.com/paulus/maximocleanup/blob/master/script/cleanupgeneric.py)

##2. Create Action Group:
- Action: CLEANUPCOMMLOG_GRP
- Action Description: Cleanup Communication Log - Group
- Type: Action Group
- Members: CLEANUPCOMMLOG

##3. Create Escalation:
- Escalation: CLEANUPCOMMLOG
- Description: Cleanup Communication Log
- Schedule: Adjust as needed
- Condition: type the 'where clause' condition as needed. 

Add one (1) escalation point with Action Group: CLEANUPCOMMLOG_GRP
*(Optional)* Tick Repeat box as needed

**Important**: 
- Ensure the condition only select the records that you intend to delete!
- Deactivate the escalation when it is not being used

#Prepare Cleanup for Workflow Instance
##1. Create Script with Action Launch Point:
- Launch Point: CLEANUPWFINSTANCE
- Description: Cleanup Workflow Instance
- Object: COMMLOG
- Action: CLEANUPWFINSTANCE
- Action Description: Cleanup Workflow Instance
- Active: Ticked
- Script: Existing (share existing script previously created for CLEANUPCOMMLOG)
- Script: browse and select CLEANUPGENERIC

##2. Create Action Group:
- Action: CLEANUPWFINSTANCE_GRP
- Action Description: Cleanup Workflow Instance - Group
- Type: Action Group
- Members: CLEANUPWFINSTANCE

##3. Create Escalation:
- Escalation: CLEANUPWFINSTANCE
- Description: Cleanup Workflow Instance
- Schedule: Adjust as needed
- Condition: type the 'where clause' condition as needed. 

Add one (1) escalation point with Action Group: CLEANUPWFINSTANCE_GRP
*(Optional)* Tick Repeat box as needed

**Important**: 
- Ensure the condition only select the records that you intend to delete!
- Deactivate the escalation when it is not being used

#Prepare Cleanup for Work Order
##1. Create Script with Action Launch Point for Work Order:
- Launch Point: CLEANUPWORKORDER
- Description: Cleanup WorkOrder
- Object: WORKORDER
- Action: CLEANUPWORKORDER
- Action Description: Cleanup WorkOrder
- Active: Ticked
- Script: New

###Continue with the next dialog for New Script Details:
- Script: CLEANUPWORKORDER
- Script Description: WorkOrder Cleanup Script
- Script Language: jython
- Source Code: import or copy the script from [cleanupworkorder.py](https://github.ibm.com/paulus/maximocleanup/blob/master/script/cleanupworkorder.py)

##2. Create Action Group:
- Action: CLEANUPWORKORDER_GRP
- Action Description: Cleanup WorkOrder - Group
- Type: Action Group
- Members: CLEANUPWORKORDER

##3. Create Escalation:
- Escalation: CLEANUPWORKORDER
- Description: Cleanup WorkOrder
- Schedule: Adjust as needed
- Condition: type the 'where clause' condition as needed. 

Add one (1) escalation point with Action Group: CLEANUPWORKORDER_GRP
*(Optional)* Tick Repeat box as needed

**Important**: 
- Ensure the condition only select the records that you intend to delete!
- Deactivate the escalation when it is not being used

#Prepare Cleanup for Ticket
##1. Create Script with Action Launch Point for Ticket:
- Launch Point: CLEANUPTICKET
- Description: Cleanup Ticket
- Object: TICKET
- Action: CLEANUPTICKET
- Action Description: Cleanup Ticket
- Active: Ticked
- Script: New

###Continue with the next dialog for New Script Details:
- Script: CLEANUPTICKET
- Script Description: Ticket Cleanup Script
- Script Language: jython
- Source Code: import or copy the script from [cleanupticket.py](https://github.ibm.com/paulus/maximocleanup/blob/master/script/cleanupticket.py)

##2. Create Action Group:
- Action: CLEANUPTICKET_GRP
- Action Description: Cleanup Ticket - Group
- Type: Action Group
- Members: CLEANUPTICKET

##3. Create Escalation:
- Escalation: CLEANUPTICKET
- Description: Cleanup Ticket
- Schedule: Adjust as needed
- Condition: type the 'where clause' condition as needed.

Add one (1) escalation point with Action Group: CLEANUPTICKET_GRP
*(Optional)* Tick Repeat box as needed

**Important**: 
- Ensure the condition only select the records that you intend to delete!
- Deactivate the escalation when it is not being used

#Sample Usage:
####1. Cleanup WorkOrder #1234:
1. Update Condition of CLEANUPCOMMLOG Escalation:<br>
`ownerid in (select workorderid from workorder where wonum='1234' and woclass='WORKORDER') and ownertable='WORKORDER'`

2. Update Condition of CLEANUPWFINSTANCE Escalation:<br>
`ownerid in (select workorderid from workorder where wonum='1234' and woclass='WORKORDER') and ownertable='WORKORDER'`

3. Update Condition of CLEANUPWORKORDER Escalation:<br>
`wonum='1234' AND woclass='WORKORDER'`

4. Activate the Escalations: CLEANUPCOMMLOG, CLEANUPWFINSTANCE, CLEANUPWORKORDER

5. Verify the result and Deactivate the Escalations: CLEANUPCOMMLOG, CLEANUPWFINSTANCE, CLEANUPWORKORDER

####2. Cleanup Service Request (SR) Ticket that has CLOSED status:
1. Update Condition of CLEANUPCOMMLOG Escalation:<br>
`ownerid in (select ticketuid from ticket where status='CLOSED' and class='SR') and ownertable='SR'`

2. Update Condition of CLEANUPWFINSTANCE Escalation:<br>
`ownerid in (select ticketuid from ticket where status='CLOSED' and class='SR') and ownertable='SR'`

3. Update Condition of CLEANUPTICKET Escalation:<br>
`status='CLOSED' and class='SR'`

4. Activate the Escalations: CLEANUPCOMMLOG, CLEANUPWFINSTANCE, CLEANUPTICKET

5. Verify the result and Deactivate the Escalations: CLEANUPCOMMLOG, CLEANUPWFINSTANCE, CLEANUPTICKET
