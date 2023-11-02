def solution():
    dough_length = 12
    dough_width = 12
    biscuit_length = 3
    biscuit_width = 3

    # Calculate the number of biscuits that can fit along the length and width of the dough
    num_biscuits_length = dough_length // biscuit_length
    num_biscuits_width = dough_width // biscuit_width

    # Calculate the total number of biscuits that can be made with the sheet of dough
    total_biscuits = num_biscuits_length * num_biscuits_width
    result = total_biscuits
    return result

print(solution())