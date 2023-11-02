def solution():
    cost_first_pair = 22
    cost_second_pair = cost_first_pair * 1.5  # 50% more expensive

    # Calculate the total cost of both pairs of shoes
    total_cost = cost_first_pair + cost_second_pair
    result = total_cost
    return result

print(solution())