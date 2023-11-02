def solution():
    # Calculate the total cost of the robots
    robot_cost = 8.75 * 7

    # Calculate the total cost with tax added
    total_cost = robot_cost + 7.22

    # Calculate the amount Austin paid
    amount_paid = total_cost - 11.53

    # Calculate the starting amount
    starting_amount = amount_paid + total_cost
    result = starting_amount
    return result

print(solution())