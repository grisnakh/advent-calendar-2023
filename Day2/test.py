import re

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
    minimum_numbers = {color: min(counts) for color, counts in color_counts.items()}

    return minimum_numbers

input_string = "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"
result = extract_minimum_numbers(input_string)

print("Minimum numbers needed for each color:")
for color, count in result.items():
    print(f"{color}: {count}")