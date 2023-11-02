def solution():
    num_friends = 7  # Austin bought 7 robots
    cost_per_robot = 8.75  # Each robot costs $8.75
    total_cost_before_tax = num_friends * cost_per_robot  # Total cost before tax
    total_cost_after_tax = total_cost_before_tax + 7.22  # Total cost after tax
    starting_money = total_cost_after_tax + 11.53  # Starting money includes the total cost and change received
    result = starting_money
    return result

print(solution())