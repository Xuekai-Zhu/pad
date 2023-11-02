def solution():
    # Calculate the total cost of the pills
    cost_of_4_pills = 4 * 1.5  # 4 of the pills cost $1.50 each
    total_pills_minus_4 = 9 - 4  # number of pills that cost $5.50 more
    cost_of_total_pills_minus_4 = total_pills_minus_4 * 5.5  # cost of pills that cost $5.50 more
    total_cost = (cost_of_4_pills + cost_of_total_pills_minus_4) * 14  # cost for 14 days of pills

    result = total_cost
    return result

print(solution())