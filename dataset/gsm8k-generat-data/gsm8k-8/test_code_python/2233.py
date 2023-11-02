def solution():
    # Define the number of croissants, cakes, and pizzas eaten by each person
    croissants_per_person = 7
    cakes_per_person = 18
    pizzas_per_person = 30

    # Calculate the total number of croissants, cakes, and pizzas consumed by both people
    total_croissants = croissants_per_person * 2
    total_cakes = cakes_per_person * 2
    total_pizzas = pizzas_per_person * 2

    # Calculate the sum of all the food items
    food_sum = total_croissants + total_cakes + total_pizzas
    result = food_sum
    return result

print(solution())