def solution():
    num_singers = 30  # The choir has 30 members
    current_robes = 12  # The choir currently has 12 robes
    remaining_robes = num_singers - current_robes  # The choir needs to buy the remaining robes
    robe_cost = 2  # Each robe costs $2

    # Calculate the total cost of the remaining robes
    total_cost = remaining_robes * robe_cost
    result = total_cost
    return result

print(solution())