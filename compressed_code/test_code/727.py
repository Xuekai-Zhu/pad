def solution():
    
    sheet_width = 12
    sheet_height = 12
    biscuit_width = 3
    biscuit_height = 3
    num_biscuits_width = sheet_width // biscuit_width
    num_biscuits_height = sheet_height // biscuit_height
    total_biscuits = num_biscuits_width * num_biscuits_height
    result = total_biscuits
    return result

print(solution())