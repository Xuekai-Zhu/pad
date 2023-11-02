def solution():
    initial_number_of_pets = 16
    number_of_pets_lost = 6
    number_of_pets_dead = initial_number_of_pets / 5
    number_of_pets_left = initial_number_of_pets - number_of_pets_lost - number_of_pets_dead
    result = number_of_pets_left
    return result

print(solution())