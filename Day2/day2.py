import re

file_path = './input.txt'

test_file_path = './testInput.txt'

print("Reading file")

RED_CUBES = 12
GREEN_CUBES = 13
BLUE_CUBES = 14

color_mapper = {
    "red": 12,
    "green": 13,
    "blue": 14
}

with open(test_file_path, 'r') as file:
    games = file.read().split('\n')

games = [game for game in games if game]

def extract_numerical(string):
    # Using regular expression to extract numerical part
    numerical_part = re.search(r'\d+', string)
    
    # Check if a numerical part was found
    if numerical_part:
        return numerical_part.group()
    else:
        return None

def extract_non_numerical_iterative(string):
    # Iterating through characters in the string and collecting non-digits
    non_numerical_part = ''.join(char for char in string if not (char.isdigit() or char.isspace()))
        
    return non_numerical_part

def split_string(string, delimiter):
    return string.split(delimiter)

def extract_minimum_numbers(input_string):
    color_counts = {}

    # Extract color counts using regular expression
    matches = re.findall(r'(\d+)\s+(\w+)', input_string)

    for count, color in matches:
        count = int(count)
        if color in color_counts:
            color_counts[color].append(count)
        else:
            color_counts[color] = [count]

    # Find the minimum number needed for each color
    minimum_numbers = {color: max(counts) for color, counts in color_counts.items()}

    return minimum_numbers


gameIDs = []
game_dict = {}
tmp_dict = []

for game in games:
    print(game)
    
    initialSplit = split_string(game, ":")
    
    gameName = initialSplit[0]
    gameID = extract_numerical(gameName)
    
    game_dict[gameID] = []
    
    separate_guesses = split_string(initialSplit[1] , ";")
    
    game_string = initialSplit[1].replace(";", ',');
    
    tmp_mult = 1
    result = extract_minimum_numbers(game)
    for key, value in result.items():
        tmp_mult *= value
    tmp_dict.append(tmp_mult)
        
    print(result)
    print(tmp_dict)

    for guess in split_string(game_string, ","):
        number_of_cubes = extract_numerical(guess)
        cubes_color = extract_non_numerical_iterative(guess)

sum = 0
for value in tmp_dict:
    sum += value
    
print(sum)
    
    
    
    
    
    
    
    
    
    