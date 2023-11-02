def solution():
    # Calculate the total cost of the plates
    plates_cost = 9 * 2  # 9 plates at $2 each

    # Calculate the cost of the spoons
    spoon_cost = 24 - plates_cost  # total cost - plates cost

    # Calculate the number of spoons
    num_spoons = spoon_cost / 1.5  # spoons at $1.50 each

    result = num_spoons
    return result

print(solution())