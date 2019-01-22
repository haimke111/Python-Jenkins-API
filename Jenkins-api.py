import jenkins
import sys
import json
#Jenkins-api - exploring the wonders of the jenkins-api plugin for python.
#Created by Haimke
#19.1.2019

str2 = "-------------------------------------------------------"
str3 = "[INFO]"
server = jenkins.Jenkins('http://35.239.139.157/jenkins/', username='user', password='user')
user = server.get_whoami()

version = server.get_version()
print('Hello %s from Jenkins %s' % (user['fullName'], version))
jobs = server.get_job_info(sys.argv[1],0,True)
#print( jobs)
output = server.get_build_console_output(sys.argv[1],int(sys.argv[2]))
output = output[int(output.find(str2)):]
build_info = server.get_build_info(sys.argv[1],int(sys.argv[2]))
#started = build_info["shortDescription"]
duration = build_info["duration"]
status = build_info["result"]
print("Started by: " )
print("Status: ",status)
print("Duration(ms): ",duration)
print("Slave: ")
#printing the test results. not sure if that's what you meant, and if so - what part of the results to print.. (but that's easy to change)
print("Tests result: ",output[int(output.find(str2)):int(output.find(str3))])

