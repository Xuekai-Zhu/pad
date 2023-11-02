def solution():
    """Tom decides to get a new floor for his room. It cost $50 to remove the floor. The new floor costs $1.25 per square foot and Tom's room is 8*7 feet. How much did it cost to replace the floor?"""
    remove_cost = 50
    length = 8
    width = 7
    area = length * width
    cost_per_square_foot = 1.25
    replacement_cost = area * cost_per_square_foot + remove_cost
    result = replacement_cost
    return result

print(solution())