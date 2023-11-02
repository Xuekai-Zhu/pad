def solution():
    num_ladders_50 = 10
    rungs_50 = 50
    num_ladders_60 = 20
    rungs_60 = 60
    cost_per_rung = 2.0

    # Calculate the total number of rungs needed for all 50 rung ladders
    total_rungs_50 = num_ladders_50 * rungs_50

    # Calculate the total number of rungs needed for all 60 rung ladders
    total_rungs_60 = num_ladders_60 * rungs_60

    # Calculate the total cost of all ladders
    total_cost = (total_rungs_50 + total_rungs_60) * cost_per_rung
    result = total_cost
    return result

print(solution())