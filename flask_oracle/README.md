**Flask REST Service over Oracle Database**  
Parameters: schema_name, table_name  
Route: /get_table_content  
Usage example: http://127.0.0.1:5000/get_table_content?schema=hr&table=COUNTRIES  

**HOWTO:**  
***Setup***  
1. Download and unzip Oracle Instant Client. Path to folder of Oracle Instant Client is using as value for ORACLE_HOME environment variable    
2. Create file $ORACLE_HOME/network/admin/tnsnames.ora with content like this:    
```
XE =  
  (DESCRIPTION =  
    (ADDRESS = (PROTOCOL = TCP)(HOST = localhost)(PORT = 1251))  
    (CONNECT_DATA =  
      (SERVER = DEDICATED)
      (SERVICE_NAME = xepdb1)
    )
  )
```
3. Install the following python's packages:  flask, cx_Oracle, requests  

***Run***  
```
python ./flask_oracle.py
```
