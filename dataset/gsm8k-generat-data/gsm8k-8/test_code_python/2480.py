def solution():
    # Define number of singers and current number of robes
    num_singers = 30
    current_robes = 12

    # Calculate how many robes need to be bought
    robes_to_buy = num_singers - current_robes

    # Calculate the total cost of the robes
    total_cost = robes_to_buy * 2
    result = total_cost
    return result

print(solution())