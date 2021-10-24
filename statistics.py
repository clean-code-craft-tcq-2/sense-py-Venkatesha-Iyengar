import sys
import math

def calculateStats(numbers):
    #Define a dictionary for returning the output
    output_dictionary = dict()

    #Check if the list is empty or not
    if not len(numbers)==0:

        try:
            #Compute the statistics
            output_dictionary['avg'] = sum(numbers) / len(numbers)
            output_dictionary['min'] = min(numbers)
            output_dictionary['max'] = max(numbers)
            
        except Exception as reason:
            print("Calculating statistics failed with reason\n")
            print(reason)
            sys.exit(1)

    else:
        #Return all the values as nan
        output_dictionary['avg'] = math.nan
        output_dictionary['min'] = math.nan
        output_dictionary['max'] = math.nan

    return output_dictionary

#Defining a class for LED Alert
class LEDAlert:
    #Init function to initialise the object to the class
    def __init__(self):
        #Define the variable for the class and initialise to False by default
        #LED glows only when threshold is crossed. Hence Off by default
        self.ledGlows = False 

#Defining a class for Email Alert
class EmailAlert:
    #Init function to initialise the object to the class
    def __init__(self):
        #Define the variable for the class and initialise to False by default
        #Email sent only when threshold is crossed. Hence False by default
        self.emailSent=False 

#Defining a class for StatsAlerter
class StatsAlerter:
    #Init function to initialise the object to the class
    #For this class, two arguments are passed during initialisation of object.
    def __init__(self, Threshold_value, Object_list_alerts):
        self.Threshold_value = Threshold_value
        self.Object_list_alerts = Object_list_alerts

    #Function to check and alert if the threshold is crossed
    def checkAndAlert(self, values):
        #Check if any value is greater than the threshold value
        if max(values) > self.Threshold_value:

            #Send Email and LED should turn ON
            self.Object_list_alerts[0].emailSent = True
            self.Object_list_alerts[1].ledGlows = True

        else:
            #Email should not be sent and LED should turn OFF
            self.Object_list_alerts[0].emailSent = False
            self.Object_list_alerts[1].ledGlows = False
