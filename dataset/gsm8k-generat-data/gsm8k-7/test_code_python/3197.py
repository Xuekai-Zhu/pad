def solution():
    starting_pets = 16
    lost_pets = 6
    remaining_pets = starting_pets - lost_pets
    died_pets = remaining_pets * (1/5)
    remaining_pets = remaining_pets - died_pets
    result = remaining_pets
    return result

print(solution())