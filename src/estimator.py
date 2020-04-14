def estimator(data):
    #initialization of variables used
    impact = {}
    severeImpact = {}
    reportedCases = data['reportedCases']
    periodType = data['periodType']
    timeToElapse = data['timeToElapse']
    totalHospitalBeds = data['totalHospitalBeds']
    avgDailyIncome = data['region']['avgDailyIncomeInUSD']
    avgDailyIncomePopulation = data['region']['avgDailyIncomePopulation']

    
    #CHALLENGE 1

    duration = duration_to_days(periodType, timeToElapse)
    factor = duration//3

    #For Impact
    impact['currentlyInfected'] = reportedCases * 10
    impact['infectionsByRequestedTime'] = impact['currentlyInfected'] * (pow(2,factor))

    #For Severe Impact
    severeImpact['currentlyInfected'] = reportedCases * 50
    severeImpact['infectionsByRequestedTime'] = severeImpact['currentlyInfected']*(pow(2,factor))

    #CHALLENGE 2

    #For Impact
    impact['severeCasesByRequestedTime'] = int(impact['infectionsByRequestedTime'] * 0.15) 
    impact['hospitalBedsByRequestedTime'] = beds_available(totalHospitalBeds, impact['severeCasesByRequestedTime'])


    #For Severe Impact
    severeImpact['severeCasesByRequestedTime'] = int(severeImpact['infectionsByRequestedTime'] * 0.15)
    severeImpact['hospitalBedsByRequestedTime'] = beds_available(totalHospitalBeds, severeImpact['severeCasesByRequestedTime'])

    #CHALLENGE 3
    

    #For Impact
    impact['casesForICUByRequestedTime'] = int(impact['infectionsByRequestedTime'] * 0.05)
    impact['casesForVentilatorsByRequestedTime'] = int(impact['infectionsByRequestedTime'] * 0.02)
    impact['dollarsInFlight'] =int((impact['infectionsByRequestedTime'] * avgDailyIncomePopulation * avgDailyIncome)/ duration)

    #For Severe Impact
    severeImpact['casesForICUByRequestedTime'] =  int(severeImpact['infectionsByRequestedTime'] * 0.05)
    severeImpact['casesForVentilatorsByRequestedTime'] = int(severeImpact['infectionsByRequestedTime'] * 0.02)
    severeImpact['dollarsInFlight'] = int((severeImpact['infectionsByRequestedTime'] * avgDailyIncomePopulation * avgDailyIncome) /duration)




    output = {'data':data, 'impact':impact, 'severeImpact': severeImpact}

    return output

def duration_to_days(durationType ,time):
    if durationType == "months":
        time *= 30
    elif durationType == "weeks":
        time *= 7

    return time

#calculating the number of beds available
def beds_available(totalbeds, severecases):
    available_beds = (0.35 * totalbeds) - severecases
    #return the available beds as integers and not floats
    return int(available_beds)