Technical Assignment - REST API

Problem:

Acme Inc. wants to distribute product documentation along with their software. Documentation is created in plain text files. However, Acme Inc. wants to make sure that these files do not contain text which infringes copyrights and trademarks. Now they need a simple solution which scans for certain trademarked names in a given text file and appends ® to trademark.

For example:
Oracle becomes Oracle® 
Unicode becomes Unicode® 


Typical line in a documentation looks like this:

Restart Oracle database after installation of patch#25.

This line becomes:
Restart Oracle® database after installation of patch#25.

All trademarked keywords are given in a flat file which is as follows:

Keyword.txt
Oracle
Unicode
Microsoft
SAP
Unicode

This file can be extended with more keywords in the future.

You need to develop a RESTful service hosted on AWS or Heroku which takes a text file as input and outputs a file with ® appended to all trademarked items. You should also log how many times your service has been called.

We should be able to test your RESTful service with curl or Postman like tool.

#############

MAN:
Home page: # curl http://<IP>:5000/
List the keywords in use: # curl [-X GET] http://<IP>:5000/keywords/
Add new keyword to Keyword.txt file: # curl -X POST http://<IP>:5000/keywords/add/<new_name>
Remove keyword from Keyword.txt file: # curl -X POST http://<IP>:5000/keywords/remove/<name>
Append ® to names listed in Keyword.txt file: # curl -X POST http://<IP>:5000/replace/<text>

