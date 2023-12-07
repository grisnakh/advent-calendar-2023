import re

file_path = './input.txt'

test_file_path = './test.txt'

print("Reading file")

with open(test_file_path, 'r') as file:
    lines = file.read()

tmp_input_arr = [line for line in lines if line]

#print(tmp_input_arr)

# Split the input string into lines
tmp_lines_arr = lines.strip().split('\n')

# Get the length of the first non-empty line
horizontal_length = len(next(line for line in tmp_lines_arr if line.strip()))

#print(f"The horizontal length of the input is: {horizontal_length}")    
        
        
input_str = """
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
"""

#[
#    [467, '.', '.', 114, '.', '.'], 
#    ['.', '.', '.', '*', '.', '.', '.', '.', '.', '.'], 
#    ['.', '.', 35, '.', '.', 633, '.'], 
#    ['.', '.', '.', '.', '.', '.', '#', '.', '.', '.'], 
#    [617, '*', '.', '.', '.', '.', '.', '.'], 
#    ['.', '.', '.', '.', '.', '+', '.', 58, '.'], 
#    ['.', '.', 592, '.', '.', '.', '.', '.'],
#    ['.', '.', '.', '.', '.', '.', 755, '.'], 
#    ['.', '.', '.', '$', '.', '*', '.', '.', '.', '.'], 
#    ['.', 664, '.', 598, '@', '.'],
#    ['.', 664, '.', '.', '.', "44", "@"],
#]

#col_index + len(value) - 1

tmp_lines_arr = lines.strip().split('\n')
horizontal_length = len(next(line for line in tmp_lines_arr if line.strip()))

rows = lines.strip().split('\n')

final_parts_array = []
# Create the array
result_array = []
for row in rows:
    result_row = []
    current_digit = ""
    for char in row:
        if char.isdigit():
            current_ digit += char
        else:
            if current_digit:
                result_row.append(int(current_digit))
                current_digit = ""
            result_row.append(char)
    if current_digit:
        result_row.append(int(current_digit))
    result_array.append(result_row)

    
    
def check_left(value, x, y):
    print(value, x, y)
    
def check_right(value, x, y):
    print(value, x, y)
    
# Display the array

def check_if_symbol(item):
    if isinstance(item, int) or (isinstance(item, str) and item.isdigit()):
        return False
    elif item == '.':
        return False
    else:
        return True
    
def get_starting_position(row, col_index):
    if (col_index  <= 0):
        return 0
    length_until_value_start = 0
    for dx in row[0:col_index]:
        length_until_value_start += len(str(dx))
    
    return length_until_value_start;
    
    
    
for row_index, row in enumerate(result_array):
    for col_index, value in enumerate(row):
        
        value_length = len(str(value))

        
        # check if is number
        if isinstance(value, (int, float)):
            value_length = len(str(value))
    
            position_value_start = get_starting_position(row, col_index)
            
            #CHECK LEFT
            left_item = row[col_index - 1] if position_value_start > 0 else None
            if (check_if_symbol(left_item) and (left_item is not None)):
                final_parts_array.append(value)
            
            #CHECK RIGHT
            right_item = row[col_index + 1] if col_index < len(row) - 1 else None 
            if (check_if_symbol(right_item) and (right_item is not None)):
                final_parts_array.append(value)
            
#            left_item = row[col_index - 1] if col_index > 0 else None
            
            #CHECK TOP
            top_list = []
            top_x = 0
            top_y_start = 0
            top_y_end = 0
            if(row_index !=0):     
                top_x = row_index - 1
                
                top_y_start = position_value_start - 1 if position_value_start > 0 else 0
                
                top_y_end = position_value_start + len(str(value)) + 1 if position_value_start + len(str(value)) < horizontal_length else horizontal_length
                
                
                
                
                
 
            print(
                "value", value,
                "position_value_start", position_value_start,
                "top_x", top_x,
                "top_y_start", top_y_start,
                "top_y_end", top_y_end,
                "top_check", result_array[top_x][int(top_y_start):int(top_y_end)]
#                "left_item", left_item,
#                "right_item", right_item,
#                "position_value_start", position_value_start,
#                "horizontal_length", horizontal_length,
#                "Row length:", len(row), 
#                "Column index", col_index
            )

                
sum = 0
for value in final_parts_array:
    sum += value
    
print("Final parts array", final_parts_array)
print("Final sum", sum)