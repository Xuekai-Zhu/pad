def solution():
    # Calculate the number of pickles Phillip can make
    num_pickles = min(10*6, 4*12)  # Phillip has enough supplies to make the lesser of the two amounts
    # Calculate the total amount of vinegar used
    total_vinegar = num_pickles/12 * 10  # each jar of pickles requires 10 ounces of vinegar
    # Calculate the amount of vinegar left
    vinegar_left = 100 - total_vinegar
    result = vinegar_left
    return result

print(solution())