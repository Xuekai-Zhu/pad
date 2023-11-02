def solution():
    monicas_money = 15
    michelles_money = 12
    cake_cost = 15
    soda_cost = 3
    soda_servings = 12
    total_money = monicas_money + michelles_money
    total_guests = 8
    total_soda_cost = total_money - cake_cost
    total_soda = total_soda_cost / soda_cost
    servings_per_person = total_soda * soda_servings / total_guests
    result = servings_per_person
    return result

print(solution())