def solution():
    """Unique is making biscuits. She has a sheet of dough that is 12 inches by 12 inches. She makes square biscuits and each biscuit is 3 inches by 3 inches. How many biscuits can she make with this dough?"""
    # Determine the area of the dough sheet
    dough_area = 12 * 12

    # Determine the area of each biscuit
    biscuit_area = 3 * 3

    # Determine the maximum number of biscuits that can be made
    max_biscuits = dough_area // biscuit_area

    # Display the maximum number of biscuits that can be made
    result = max_biscuits
    return result

print(solution())