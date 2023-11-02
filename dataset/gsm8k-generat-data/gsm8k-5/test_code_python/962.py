def solution():
    dough_area = 12 * 12  # The dough is 12 inches by 12 inches
    biscuit_area = 3 * 3  # Each biscuit is 3 inches by 3 inches

    # Calculate the maximum number of biscuits Unique can make
    max_biscuits = dough_area // biscuit_area

    result = max_biscuits
    return result

print(solution())