def solution():
    # cost for first apartment
    rent1 = 800
    utilities1 = 260
    driving_cost1 = 20 * 31 * 0.58  # 20 days of 31 miles at $0.58/mile
    total_cost1 = rent1 + utilities1 + driving_cost1

    # cost for second apartment
    rent2 = 900
    utilities2 = 200
    driving_cost2 = 20 * 21 * 0.58  # 20 days of 21 miles at $0.58/mile
    total_cost2 = rent2 + utilities2 + driving_cost2

    # calculate the difference in total monthly costs
    difference = round(total_cost2 - total_cost1)
    result = difference
    return result

print(solution())