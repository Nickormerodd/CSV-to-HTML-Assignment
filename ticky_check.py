#!/usr/bin/env python3
"""
Author: Nick Ormerod
Date: 28/ 11/ 2002
Ticky_check.py is the main code for this example where we read through each error and each user in the file in the syslog.log file.
Completed using hints and guidance from the course.

Write a script to generate two different reports based on the ranking of errors generated by the
system and the user usage statistics for the service. After importing the necessary modules, initialize 
two dictionaries: one for the number of different error messages and another to count the number of entries 
for each user (splitting between INFO and ERROR).Then parse through each log entry in the syslog.log file by iterating over the file.
For each log entry, you'll have to first check if it matches the INFO or ERROR message formats. 
You should use regular expressions for this. When you get a successful match, add one to the corresponding value in the per_user dictionary.
If you get an ERROR message, add one to the corresponding entry in the error dictionary by using proper data structure.
After you've processed the log entries from the syslog.log file, you need to sort both the per_user and error dictionary before
creating CSV report files.

After sorting these dictionaries, store them in two different files: error_message.csv and user_statistics.csv.
"""
import re
import sys
import operator
import csv

per_user = {}
error = {}

logfile = open("syslog.log")

for line in logfile:
    line = line.strip()
    username = (re.search(r"\((.*)\)", line)).group(1)
    message = (re.search(r"(ERROR|INFO)", line)).group(1)
    user_count = {"INFO": 0, "ERROR": 0}
    if (username not in per_user):
        per_user[username] = user_count
    per_user[username][message] += 1

    if message == "ERROR":
        system_error = (re.search(r"ERROR (.*) ", line)).group(1)
        if (system_error not in error):
            error[system_error] = 0
        error[system_error] += 1
logfile.close()


sorted_per_user = []
sorted_error = []

for key in sorted(per_user.keys()):
    sorted_per_user.append(
        [key, per_user[key]["INFO"], per_user[key]["ERROR"]])

for key, value in sorted(error.items(), key=lambda item: item[1], reverse=True):
    sorted_error.append([key, value])

sorted_per_user.insert(0, ["Username", "INFO", "ERROR"])
sorted_error.insert(0, ["Error", "Count"])

error_messages_file = open("error_message.csv", "w")
user_statistics_file = open("user_statistics.csv", "w")

writer1 = csv.writer(error_messages_file)
writer1.writerows(sorted_error)

writer2 = csv.writer(user_statistics_file)
writer2.writerows(sorted_per_user)

error_messages_file.close()
user_statistics_file.close()
