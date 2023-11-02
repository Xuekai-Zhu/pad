def solution():
    cup_to_ml = 250
    milk_per_serving = 0.5
    servings_per_person = 2
    persons = 6
    total_servings = persons * servings_per_person
    total_milk = total_servings * milk_per_serving
    total_litres = total_milk / 1000
    total_cartons = total_litres / 1
    result = total_cartons
    
    return result

print(solution())