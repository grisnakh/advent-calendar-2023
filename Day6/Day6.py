races = [{
    "time": 59,
    "recordDistance": 543
},{
    "time": 68,
    "recordDistance": 1020
},{
    "time": 82,
    "recordDistance": 1664
},{
    "time": 74,
    "recordDistance": 1022
}]

oneRaceToRuleThemAll = [{
    "time": 59688274,
    "recordDistance": 543102016641022
}]

#my_list = [10, 20, 30, 40, 50]
#for i in range(len(my_list)):
#    # Your code here
#    print(f"Index: {i}, Value: {my_list[i]}")

#for index, pressButtonDuration in enumerate(testRace["time"]):

def calcCoveredDistance(currentSpeed, timeRemaining):
    return currentSpeed * timeRemaining

finalComboCounts = list()
for race in oneRaceToRuleThemAll:
    
    coveredDistance = 0
    givenTime = race["time"]
    givenRecordDistance = race["recordDistance"]

    winnerCombo = list()

    for pressButtonDuration in range(givenTime):
        currentSpeed = pressButtonDuration

        coveredDistance = calcCoveredDistance(currentSpeed, race["time"] - pressButtonDuration)
        if (coveredDistance > givenRecordDistance):
            winnerCombo.append(pressButtonDuration)
    
    
    finalComboCounts.append(len(winnerCombo))


req = 1
for value in finalComboCounts:
    req *= value
    
print(req)