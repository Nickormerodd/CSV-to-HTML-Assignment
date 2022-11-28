# Google-IT_Automation

Using Python to Interact with the Operating System

Imagine your company uses a server that runs a service called ticky, an internal ticketing system. The service logs events to syslog, both when it runs successfully and when it encounters errors.

The service's developers need your help getting some information from those logs so that they can better understand how their software is used and how to improve it. So, for this lab, you'll write some automation scripts that will process the system log and generate reports based on the information extracted from the log files.

What you'll do
-Use regex to parse a log file
-Append and modify values in a dictionary
-Write to a file in CSV format
-Move files to the appropriate directory for use with the CSV->HTML converter

./csv_to_html.py user_statistics.csv /var/www/html/userfile.html 
or
./csv_to_html.py error_message.csv /var/www/html/errorfile.html
are the commands in the shell that can be executed to convert the selected csv into an html
