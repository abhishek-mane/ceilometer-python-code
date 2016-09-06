'''
    This is starting point of the code
    This file uses command line arguments.
    Run this file as
        $ python Main.py jsonfile.json
'''
import sys
import json
from CeiloMeterClient import CeiloMeterClient
from template import Template

if (len(sys.argv) != 2):
    print "please specify json file as input in cmd line arguments. exiting..."
    exit(1)

inputData = json.loads(open(str(sys.argv[1])).read())
ceilometerClient = CeiloMeterClient(inputData)
listOfMeters = ceilometerClient.query()
Template.render(listOfMeters, "output.html")
