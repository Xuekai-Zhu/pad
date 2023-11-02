def solution():
    # Calculate the cost of two black printer inks
    black_ink_cost = 11 * 2

    # Calculate the cost of three red printer inks
    red_ink_cost = 15 * 3

    # Calculate the cost of two yellow printer inks
    yellow_ink_cost = 13 * 2

    # Calculate the total cost of all the printer inks
    total_ink_cost = black_ink_cost + red_ink_cost + yellow_ink_cost

    # Calculate the difference between the cost of printer inks and the amount given by Phantom's mom
    difference = total_ink_cost - 50

    result = difference
    return result

print(solution())