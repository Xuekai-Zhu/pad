def solution():
    initial_number_of_animals = 68
    animals_gained = 6 + 1 + 3 + 2
    animals_lost = 0
    total_number_of_animals = initial_number_of_animals + animals_gained - animals_lost
    result = total_number_of_animals - 68
    return result

print(solution())