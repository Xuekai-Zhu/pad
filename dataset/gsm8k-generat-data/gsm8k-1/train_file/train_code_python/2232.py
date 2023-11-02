def solution():
    """Jorge and Giuliana each eat 7 croissants for breakfast, 18 cakes after school, and 30 pizzas before bedtime. What is the total number of croissants, cakes, and pizzas the two consume in a day?"""
    croissants_per_person = 7
    cakes_per_person = 18
    pizzas_per_person = 30
    total_croissants = croissants_per_person * 2
    total_cakes = cakes_per_person * 2
    total_pizzas = pizzas_per_person * 2
    total_consumed = total_croissants + total_cakes + total_pizzas
    result = total_consumed
    return result

print(solution())