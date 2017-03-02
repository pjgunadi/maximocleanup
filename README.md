# Maximo Cleanup
IBM Maximo automation scripts (Jython) to cleanup MBOs such as Work Order, Ticket, and Asset

# Background
Certain maximo MBOs do not allow deletion after activities have been committed to the record such as change of status, applied workflow, and communication log
This behaviour could be expected in production environment. However, at some development and test environment, maximo designer may need to delete records after test activities.
This library has some script that may help the record deletion without needing to reinstall new maximo.
