KgToTonne = 0.001
TonneToKg = 1000
KgToPound = 2.20462
PoundToKg = 1/KgToPound

def kgtotonne(kg):
    return kg * KgToTonne

def tonnetokg(tonne):
    return tonne * TonneToKg

def kgtopound(kg):
    return kg * KgToPound

def poundtokg(pound):
    return pound * PoundToKg

def help():
    print("----------MASS CONVERSION MODULE DETAILS----------")
    print("List of available functions along with their respective descriptions:")
    print("- kgtotonne(kg): Convert Kilograms into tonne")
    print("- tonnetokg(tonne): Coonvert tonne into kilograms")
    print("- kgtopound(kg): Convert kilograms into pound")
    print("- poundtokg(pound): Convert pound into kilograms\n")
    print("Constants used:")
    print("1 tonne = 1000 kilograms")
    print("1 kg = 2.20462 Pound")