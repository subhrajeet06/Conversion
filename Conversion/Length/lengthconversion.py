mile_to_km = 1.609344
km_to_mile = 1/mile_to_km
feet_to_inches = 12
inches_to_feet = 1/feet_to_inches

def miletokm(mile):
    km = mile_to_km * mile
    return km

def kmtomile(km):
    mile = km * km_to_mile
    return mile

def feettoinches(feet):
    inch = feet_to_inches * feet
    return inch

def inchestofeet(inch):
    feet = inch * inches_to_feet
    return feet

def help():
    print("----------LENGTH CONVERSION MODULE DETAILS----------")
    print("List of available functions along with their respective descriptions:")
    print("- miletokm(mile): Convert miles into kilometres")
    print("- kmtomile(km): Coonvert Kilometer into miles")
    print("- feettoinches(feet): Convert feet into inches")
    print("- inchestofeet(inch): Convert inch into feet\n")
    print("Constants used:")
    print("1 mile = 1.609344 kilometres")
    print("1 feet = 12 inches")