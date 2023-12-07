import re

file_path = './input.txt'

test_file_path = './test.txt'

print("Reading file")

with open(file_path, 'r') as file:
    lines = file.read().split('\n')

lines = [line for line in lines if line]

regex = re.compile(r'(?=(one|two|three|four|five|six|seven|eight|nine|zero|\d+))')
    
stringToNumberMapper = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}

arraOfNumbers = []
for line in lines:    
    tmp_arr = [];

    # Find all matches in the input string
    matches = regex.findall(line)
    firstNum = matches[0]
    
    if firstNum in stringToNumberMapper:
        firstNum = str(stringToNumberMapper[firstNum])
    else:
        firstNum = firstNum[0]
        
    secondNum = matches[-1]
    
    if secondNum in stringToNumberMapper:
        secondNum = str(stringToNumberMapper[secondNum])
    else:
        secondNum = secondNum[-1];

    finalNum = int(firstNum + secondNum)
   
    print("Matches:", matches, firstNum, secondNum, finalNum )
 
    arraOfNumbers.append(finalNum)

totalSum = 0
for number in arraOfNumbers:
    totalSum += number
#    print(totalSum, number)
    
print(totalSum)