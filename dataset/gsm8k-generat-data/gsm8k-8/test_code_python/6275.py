def solution():
    # Calculate the total length of rope needed in inches
    total_length = 10 * 6

    # Calculate the cost of the 6-foot length of rope
    six_foot_cost = 5

    # Calculate the cost per inch of the 6-foot length of rope
    six_foot_cost_per_inch = six_foot_cost / (6*12)

    # Calculate the cost of the equivalent length of 1-foot rope
    one_foot_cost = 1.25

    # Calculate the cost per inch of the 1-foot rope
    one_foot_cost_per_inch = one_foot_cost / 12

    # Calculate the cost of the total length of rope using the 6-foot rope
    cost_with_six_foot = total_length * six_foot_cost_per_inch

    # Calculate the cost of the total length of rope using 1-foot rope
    cost_with_one_foot = total_length * one_foot_cost_per_inch

    # Determine the least amount spent
    least_cost = min(cost_with_six_foot, cost_with_one_foot)

    result = least_cost
    return result

print(solution())