def solution():
    
    sheet_length = 12
    biscuit_length = 3
    num_of_biscuits_per_row = sheet_length // biscuit_length
    num_of_rows = num_of_biscuits_per_row
    total_num_of_biscuits = num_of_biscuits_per_row * num_of_rows
    result = total_num_of_biscuits
    return result

print(solution())