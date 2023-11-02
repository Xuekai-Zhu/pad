def solution():
    """A teacher has to order supplies for his class to do a science project. Each student needs a bow, a small bottle of vinegar and a box of baking soda.
    Bows are $5 each, a bottle of vinegar is $2 and a box of baking soda is $1. The teacher has 23 students in this class. How much will the supplies cost?"""
    bows_cost = 5
    vinegar_cost = 2
    baking_soda_cost = 1
    total_cost = (bows_cost + vinegar_cost + baking_soda_cost) * 23
    result = total_cost
    return result

print(solution())