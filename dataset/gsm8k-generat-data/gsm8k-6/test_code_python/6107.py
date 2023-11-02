def solution():
    # Calculate the total bushels needed for all the animals in the farm for a day
    total_animals = 4 + 3 + 7  # 4 cows, 3 sheep, and 7 chickens
    bushels_per_animal = 2 if total_animals <= 7 else 3  # each animal needs 2 bushels if total animals is 7 or less, otherwise they need 3 bushels
    total_bushels = total_animals * bushels_per_animal
    result = total_bushels
    return result

print(solution())