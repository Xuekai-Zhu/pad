def solution():
    # Calculate the total cost of the robots before tax
    robot_cost = 8.75 * 7  # Austin bought seven robots at $8.75 each

    # Calculate the total cost of the robots with tax
    total_cost = robot_cost + 7.22

    # Calculate the amount Austin paid
    paid_amount = total_cost - 11.53

    # Calculate the amount Austin started with
    starting_amount = paid_amount + total_cost
    result = starting_amount
    return result

print(solution())