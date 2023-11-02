def solution():
    """At Kaleb's Restaurant, a group with six adults and two children came in to eat. If each adult meal cost six dollars and each children's meal was $4, and every person ordered a soda for $2 how much was the bill?"""
    adults = 6
    children = 2
    adult_meal_cost = 6
    children_meal_cost = 4
    soda_cost = 2
    total_cost = (adults * adult_meal_cost) + (children * children_meal_cost) + ((adults + children) * soda_cost)
    result = total_cost
    return result

print(solution())