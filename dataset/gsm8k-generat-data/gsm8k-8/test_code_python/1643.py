def solution():
    # Define the number of each type of light bulb that Valerie needs
    small_bulbs_needed = 3
    large_bulbs_needed = 1

    # Define the cost of each type of light bulb
    small_bulb_cost = 8
    large_bulb_cost = 12

    # Calculate the total cost of the light bulbs that Valerie needs
    total_cost = (small_bulbs_needed * small_bulb_cost) + (large_bulbs_needed * large_bulb_cost)

    # Calculate how much money Valerie will have left over
    money_left_over = 60 - total_cost
    result = money_left_over
    return result

print(solution())