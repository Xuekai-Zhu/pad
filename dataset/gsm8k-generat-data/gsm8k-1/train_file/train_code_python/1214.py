def solution():
    """One US cup equals 250ml. Brian is making lasagna for himself, his wife, his two kids, his parents, and his wife's parents. The recipe requires 1/2 a cup of milk per serving. How many 1L cartons of milk does Brian need to buy if each person is expected to eat 2 servings?"""
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