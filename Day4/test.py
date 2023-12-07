from collections import Counter

array1 = [41, 48, 83, 86, 65,64,66,98]
array2 = [83, 86,  86, 6, 31, 54,52,51,53]

# Count occurrences of numbers in each array
counter1 = Counter(array1)
counter2 = Counter(array2)

# Find the intersection of the two counters (common elements)
common_elements = counter1 & counter2

# Sum the counts of common elements
number_of_occurrences = sum(common_elements.values())

print("Number of occurrences of the same numbers:", number_of_occurrences)
