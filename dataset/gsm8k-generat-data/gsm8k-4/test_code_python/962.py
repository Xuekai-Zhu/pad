def solution():
    """Unique is making biscuits. She has a sheet of dough that is 12 inches by 12 inches. She makes square biscuits and each biscuit is 3 inches by 3 inches. How many biscuits can she make with this dough?"""
    # Define the dimensions of the dough sheet and the biscuits
    dough_length = 12
    dough_width = 12
    biscuit_length = 3
    biscuit_width = 3

    # Calculate the number of biscuits that can fit in the length and width of the dough sheet
    biscuits_fit_length = dough_length // biscuit_length
    biscuits_fit_width = dough_width // biscuit_width

    # Calculate the total number of biscuits that can fit on the dough sheet
    total_biscuits = biscuits_fit_length * biscuits_fit_width

    # return the result
    result = total_biscuits
    return result

print(solution())