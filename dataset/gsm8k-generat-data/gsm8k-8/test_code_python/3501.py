def solution():
    # Calculate the cost of the plates
    plates_cost = 9 * 2

    # Calculate the remaining amount for spoons
    spoon_amount = 24 - plates_cost

    # Calculate the number of spoons Chenny bought
    spoons_bought = spoon_amount / 1.5
    result = spoons_bought
    return result

print(solution())