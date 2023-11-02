def solution():
    """The flowers cost $9, the clay pot costs $20 more than the flower, and the bag of soil costs $2 less than the flower. How much does it cost to plant the flowers?"""
    flower_cost = 9
    pot_cost = flower_cost + 20
    soil_cost = flower_cost - 2
    total_cost = flower_cost + pot_cost + soil_cost
    result = total_cost
    return result

print(solution())