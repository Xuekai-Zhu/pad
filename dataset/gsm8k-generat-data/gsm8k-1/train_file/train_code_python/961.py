def solution():
    """Unique is making biscuits. She has a sheet of dough that is 12 inches by 12 inches. She makes square biscuits and each biscuit is 3 inches by 3 inches. How many biscuits can she make with this dough?"""
    sheet_length = 12
    biscuit_length = 3
    num_of_biscuits_per_row = sheet_length // biscuit_length
    num_of_rows = num_of_biscuits_per_row
    total_num_of_biscuits = num_of_biscuits_per_row * num_of_rows
    result = total_num_of_biscuits
    return result

print(solution())