def solution():
    """Mark is trying to choose between two venues for a surprise party for his wife. The first venue charges a flat fee of $200, regardless of how many guests attend. While the second charges, $25 per person who attends. However, the first venue does not include food, which Mark estimates will cost $5 for each person who attends. At the second venue, food for each guest is already included in the price. How many guests are necessary for the two venues to be equal in cost?"""
    flat_fee = 200
    food_cost = 5
    per_person_cost = 25 + food_cost
    num_people = (flat_fee - food_cost) / (per_person_cost - food_cost)
    result = num_people
    return result

print(solution())