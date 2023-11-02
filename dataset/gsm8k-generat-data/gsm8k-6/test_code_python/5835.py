def solution():
    total_cost = 240000  # total cost of three necklaces and a set of earrings
    cost_earrings = 3 * cost_necklace  # cost of earrings is 3 times that of a necklace
    cost_necklaces = (total_cost - cost_earrings) / 3  # total cost of necklaces is the difference between total cost and cost of earrings, divided by 3 (since there are three necklaces)
    result = cost_necklaces
    return result

print(solution())