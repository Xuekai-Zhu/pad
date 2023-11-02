def solution():
    # Calculate the area of the dough sheet
    dough_area = 12 * 12

    # Calculate the area of each biscuit
    biscuit_area = 3 * 3

    # Calculate the number of biscuits that can fit on the sheet
    num_biscuits = dough_area // biscuit_area

    result = num_biscuits
    return result

print(solution())