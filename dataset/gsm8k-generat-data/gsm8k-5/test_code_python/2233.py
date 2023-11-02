def solution():
    # Number of croissants each person eats in a day
    croissants_per_person = 7

    # Number of cakes each person eats in a day
    cakes_per_person = 18

    # Number of pizzas each person eats in a day
    pizzas_per_person = 30

    # Total number of croissants, cakes, and pizzas they consume in a day
    total_consumption = (croissants_per_person + cakes_per_person + pizzas_per_person) * 2

    result = total_consumption
    return result

print(solution())