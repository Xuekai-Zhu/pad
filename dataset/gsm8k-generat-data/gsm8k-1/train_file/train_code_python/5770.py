def solution():
    """James buys 10 shirts and half as many pants. The shirts cost $6 each and the pants cost $8 each. How much did everything cost?"""
    num_shirts = 10
    num_pants = num_shirts / 2
    shirt_cost = 6
    pant_cost = 8
    total_cost = (num_shirts * shirt_cost) + (num_pants * pant_cost)
    result = total_cost
    return result

print(solution())