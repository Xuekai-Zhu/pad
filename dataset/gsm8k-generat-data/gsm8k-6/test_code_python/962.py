def solution():
    # Calculate the number of biscuits Unique can make
    square_area = 3 * 3  # area of each square biscuit
    sheet_area = 12 * 12  # area of the sheet of dough
    num_biscuits = sheet_area // square_area  # integer division to get the whole number of biscuits
    result = num_biscuits
    return result

print(solution())