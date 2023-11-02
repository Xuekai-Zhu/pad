def solution():
    
    cups_per_serving = 0.5
    total_people = 6
    servings_per_person = 2
    total_servings = total_people * servings_per_person
    total_cups = total_servings * cups_per_serving
    total_liters = total_cups / 4
    cartons_needed = total_liters // 1 + int(total_liters % 1 > 0)
    result = cartons_needed
    return result

print(solution())