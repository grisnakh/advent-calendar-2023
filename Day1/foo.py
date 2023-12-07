import re

input_string = "mfourjcxsvss3oneightlxh"

# Define a regular expression to match 'one' and 'eight' with potential overlap
pattern = re.compile(r'(?=(one|two|three|four|five|six|seven|eight|nine|zero|\d+))')
#pattern = re.compile(r'(?=(one|eight))')

#regex = re.compile("(one|two|three|four|five|six|seven|eight|nine|zero|\\d+)")

# Find all matches in the input string
#matches = [match.group(1) for match in pattern.finditer(input_string)]
matches = pattern.findall(input_string)
# Print the matches
print("Matches:", matches)