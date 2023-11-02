def solution():
    total_cost = 12 + (2/3) * 12  # apples were two times cheaper than oranges, so the cost of 3 kg of apples is 2/3 of the cost of 1 kg of oranges
    cost_of_apples = (total_cost - 12) / 3  # subtract the cost of oranges and divide by the weight of apples
    result = cost_of_apples
    return result

print(solution())