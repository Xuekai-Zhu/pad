def solution():
    num_friends = 7
    cost_per_robot = 8.75
    tax = 7.22
    change = 11.53

    # Calculate the total cost of all robots
    total_robot_cost = num_friends * cost_per_robot

    # Calculate the total amount Austin spent including tax
    total_spent = total_robot_cost + tax

    # Calculate the amount Austin started with
    amount_started_with = total_spent + change
    result = amount_started_with
    return result

print(solution())