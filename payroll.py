#Purpose: To create a functioning pay roll program, which can calculate your salary based
#on factors like state taxes, marital status, hourly pay, etc.

#==============================================================
#Dictionary of US states and their tax rates
#==============================================================
stateTaxes = {
    "AL": 0.035, "AK": 0.0, "AZ": 0.025, "AR": 0.0295, "CA": 0.143,
    "CO": 0.044, "CT": 0.04495, "DE": 0.044, "FL": 0.0, "GA": 0.0539,
    "HI": 0.062, "ID": 0.05695, "IL": 0.0495, "IN": 0.03, "IA": 0.038,
    "KS": 0.0539, "KY": 0.04, "LA": 0.03, "ME": 0.06475, "MD": 0.03875,
    "MA": 0.07, "MI": 0.0425, "MN": 0.076, "MS": 0.044, "MO": 0.0335,
    "MT": 0.053, "NE": 0.0383, "NV": 0.0, "NH": 0.0, "NJ": 0.06075,
    "NM": 0.037, "NY": 0.0745, "NC": 0.0425, "ND": 0.02225, "OH": 0.03125,
    "OK": 0.025, "OR": 0.07325, "PA": 0.0307, "RI": 0.0487, "SC": 0.031,
    "SD": 0.0, "TN": 0.0, "TX": 0.0, "UT": 0.0455, "VT": 0.0605,
    "VA": 0.03875, "WA": 0.0, "WV": 0.0352, "WI": 0.05575, "WY": 0.0
}

#======================================================= ==========================
#Function which allows user to type inputs, also checks if input is a valid option
#=================================================================================
def inputData():
    #Allows user to input name, also checks if name is a valid option
    while True:
        name = input("Enter Name: ")
        if name.strip() != "" and name != " ":
            print("Hello " + name)
            break
        else:
            print("Cannot leave empty")

    #=========================================================================================
    #Allows user to input weather they get payed weekly or monthly, makes calculated pay roll
    #more accurate
    #=========================================================================================
    while True:
        print("")
        payPeriod = input("Enter W for Weekly pay or M for Monthly pay: ")
        payPeriod = payPeriod.upper()
        if payPeriod.strip() == "W" or payPeriod.strip() == "M":
            break
        else:
            print("Please enter in suggested inputs")

    #=============================================================================
    #Allows user to input how many hours they worked (IMPORTANT FOR CALCULATIONS)
    #=============================================================================
    while True:
        try:
            print("")
            hoursWorked = int(input("Enter hours worked during pay period: "))
            if hoursWorked > 0:
                break
            else:
                print("Input must be greater than 0")
        except Exception as e:
            #Error message is not same as variable e, in order to be user friendly
            print("Please enter an integer")

    #====================================================================================
    #Allows user to input how much they get payed per hour (IMPORTANT FOR CALCULATIONS)
    #====================================================================================
    while True:
        try:
            print("")
            hourlyPay = int(input("Enter hourly pay with no cuts or tax reductions: "))
            if hourlyPay > 0:
                break
            else:
                print("Input must be greater than 0")
        except Exception as e:
            #Error message is not same as variable e, in order to be user friendly
            print("Please enter an integer")

    #======================================================================================
    #Allows user to enter marital status, important because states offer certain privaleges
    #depending on if your married or single
    #======================================================================================
    while True:
        print("")
        maritalStatus = input("Enter M for Married or S for Single: ")
        maritalStatus = maritalStatus.upper()
        if maritalStatus.strip() == "M" or maritalStatus.strip() == "S":
            break
        else:
            print("Please enter in suggested inputs")

    #=====================================================================================
    #Allows user to input state, states have different taxes, (IMPORTANT FOR CALCULATIONS)
    #=====================================================================================
    while True:
        print("")
        usState = input("Enter your state: ")
        usState = usState.upper()
        stateResult = checkStates(usState)
        if stateResult == "T":
            break
        else:
            print("Pleaser enter a correctly abbreviated US state")

    #Adds all inputs into a list for later use
    return[name, payPeriod, hoursWorked, hourlyPay, maritalStatus, usState]

#=============================================================================
#Function which checks if state input is valid, parameter is inputted state
#=============================================================================
def checkStates(inState):
    if inState.upper() in stateTaxes:
        return "T"
    else:
        return "F"

#================================================================================
#Calculates the federal with-holding tax based on the user's annual salary and marital status
#Brackets taken from 2021 IRS website
#Website URL: https://www.irs.gov/publications/p15t
#===============================================================================
def calculateFederalTax(salary, maritalStatus):
    taxBracketListM = [12200, 32100, 93250, 184950, 342050, 431050, 640500] #Married Bracket
    taxBracketListS = [3950, 13900, 44475, 90325, 168875, 213375, 527550] #Single Bracket
    taxRateList = [0, 0.1, 0.12, 0.22, 0.24, 0.32, 0.35, 0.37] #Tax Rates
    adjustedAmountM = [0, 12200, 32100, 93250, 184950, 342050, 431050, 640500] #Married Adjusted Amo
    adjustedAmountS = [0, 3950, 13900, 44475, 90325, 168875, 213375, 527550] #Single Adjusted Amount
    additionalFeeM = [0, 0, 1990, 9328, 25903, 67206, 95686, 168993.5] #Married Additional Amount
    additionalFeeS = [0, 0, 995, 4664, 14751, 33603, 47843, 157804.25] #Single Additional Amount
    
    lengthM = len(taxBracketListM)
    lengthS = len(taxBracketListS)
    fdtax = 0

    if maritalStatus == "M":
        for i in range(lengthM):
            if salary <= taxBracketListM[i] :
                fdtax = ((salary - adjustedAmountM[i]) * taxRateList[i]) + additionalFeeM[i]
                break
            elif i >= lengthM-1:
                i = i + 1
                fdtax = ((salary - adjustedAmountM[i]) * taxRateList[i]) + additionalFeeM[i]
        
    elif maritalStatus == "S":
        for i in range(lengthS):
            if salary <= taxBracketListS[i]:
                fdtax = ((salary - adjustedAmountS[i]) * taxRateList[i]) + additionalFeeS[i]
                break
            elif i >= lengthS-1:
                i = i + 1
                fdtax = ((salary - adjustedAmountS[i]) * taxRateList[i]) + additionalFeeS[i]
    return fdtax

#===============================================================================
#Calculates state tax based on which the state the user inputs
#NOTE: STATE TAX IS ESTIMATED
#Percentages taken from 2021 state tax rates table on NerdWallet
#Website URL: https://www.nerdwallet.com/article/taxes/state-income-tax-rates
#===============================================================================
def calculateStateTax(state):
    rate = stateTaxes.get(state.upper(), 0)  # Defaults to 0 if state not found
    stateTax = (WpayPeriod * WhoursWorked) * rate
    return stateTax

#==============================================================================
#Function which gives users the choice on Print Payroll, Re-entering, or Exiting
#Continuing will show the final payroll
#Re-entering will allow you to enter the information again
#Exiting will end the program
#===============================================================================
def optionMenu():
    while True:
        try:
            print("")
            print("================================================")
            optionsInput = (input("Enter P == Print Payroll, R == Re-enter, X == Exit"))
            optionsInput = optionsInput.upper()
            if optionsInput == "P" or optionsInput == "R" or optionsInput == "X":
                break
            else:
                print("Please enter a valid option")
        #Error message is not same as variable e, in order to be user friendly
        except Exception as e:
            print("Please enter a given letter")
    return(optionsInput)

#======================================================================
#This function calculates the initial salary without any tax cuts made
#======================================================================
def noTaxSalary():
    payPeriod = userEnterData[1]
    hoursWorked = userEnterData[2]
    hourlyPay = userEnterData[3]
    if payPeriod == "M":
        annualPay = (hoursWorked * hourlyPay) * 12
    else:
        annualPay = (hoursWorked * hourlyPay) * 52
    return(annualPay)

#=================================================================================================
#This function prints out all the values in a form similar to a receipt
#Parameters are the list stored from the input data, as well as the calculated initial and final p
#=================================================================================================
def output(myUserEnterData, myInitialPay, myFederalTax, myStateTax, mySocialSecurity, myMedicare):
    payPeriodTitle = ""
    myUserName = myUserEnterData[0]
    myHoursWorked = myUserEnterData[2]
    myHourlyPay = myUserEnterData[3]
    myUsState = myUserEnterData[5]

    if myUserEnterData[1] == "M":
        myPayPeriod = "Monthly"
        myInitialPay = myInitialPay/12
        myFederalTax = myFederalTax/12
        payPeriodTitle = "Monthly"
    else:
        myPayPeriod = "Weekly"
        myInitialPay = myInitialPay/52
        myFederalTax = myFederalTax/52
        payPeriodTitle = "Weekly"
    if myUserEnterData[4] == "S":
        myMaritalStatus = "Single"
    else:
        myMaritalStatus = "Married"

    myTotalTax = myFederalTax + myStateTax + mySocialSecurity + myMedicare
    myFinalPay = myInitialPay - myTotalTax

    print("\t----------------------------------------")
    print("\t" + payPeriodTitle + " Pay check of " + myUserName)
    print("\t----------------------------------------")
    print("\t Employee : " + myUserName)
    print("\t Pay Period : " + myPayPeriod)
    print("\t Hourly Pay : " + "{:.2F}".format(myHourlyPay))
    print("\t Marital Status : " + myMaritalStatus)
    print("\t State : " + myUsState)
    print("\t Federal Tax : " + "{:.2F}".format(myFederalTax))
    print("\t State Tax : " + "{:.2F}".format(myStateTax))
    print("\t Social Security Tax : " + "{:.2F}".format(mySocialSecurity))
    print("\t Medicare Tax : " + "{:.2F}".format(myMedicare))
    print("\t---------------------------------------")
    print("\t Initial Pay : " + "{:.2F}".format(myInitialPay))
    print("\t Total Tax : " + "{:.2F}".format(myTotalTax))
    print("\t=======================================")
    print("\t Final Pay : " + "{:.2F}".format(myFinalPay))

#=================================================================================================
#This function is used to "clear the screen" by moving all other outputs up so that it only shows
#Function is called inside the final part of program where the output function is called
#=================================================================================================
def clearScreen(line):
    print("\n" * line)

#========================================================================
#Turns inputData function and optionMenu function into global variables
#Section where functions are called and code runs
#========================================================================
while True:
    userEnterData = inputData()
    optionChoice = optionMenu()

#===============================================================================================
#if-statement makes the optionMenu function operational by only continuing if the user enter "P"
#else will make the program end since it means exit
#Reenter will happen automatically if other two inputs are given a place in the if-statement
#===============================================================================================
    if optionChoice == "P":
        WpayPeriod = userEnterData[2]
        WhoursWorked = userEnterData[3]
        initialPay = noTaxSalary()
        relationshipStatus = userEnterData[4]
        stateChoice = userEnterData[5]
        federalTax = calculateFederalTax(initialPay, relationshipStatus)
        stateTax = calculateStateTax(stateChoice)
        socialSecurity = (WpayPeriod * WhoursWorked) * 0.062
        medicare = (WpayPeriod * WhoursWorked) * 0.0145
        clearScreen(20)
        output(userEnterData, initialPay, federalTax, stateTax, socialSecurity, medicare)
        clearScreen(12)
        break
    elif optionChoice == "X":
        break
    clearScreen(30)