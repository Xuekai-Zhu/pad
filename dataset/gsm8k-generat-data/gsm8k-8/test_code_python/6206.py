def solution():
    # Define the initial costs
    table_cost = 140
    chair_cost = 100
    joystick_cost = 20

    # Divide up the costs as agreed upon
    frank_share = table_cost
    eman_share = chair_cost + (3/4) * joystick_cost

    # Calculate the difference in spending
    difference = frank_share - eman_share
    result = difference
    return result

print(solution())