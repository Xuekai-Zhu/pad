def solution():
    small_bulb_cost = 8  # Small bulbs cost $8 each
    large_bulb_cost = 12  # Large bulbs cost $12 each
    total_bulb_cost = (3 * small_bulb_cost) + (1 * large_bulb_cost)  # Calculate the total cost of bulbs
    money_left_over = 60 - total_bulb_cost  # Calculate how much money Valerie has left over
    result = money_left_over
    return result

print(solution())