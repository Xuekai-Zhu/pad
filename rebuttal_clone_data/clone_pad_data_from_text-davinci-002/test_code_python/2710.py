def solution():
    original_cows = 2
    original_pigs = 3
    original_goats = 6
    additional_cows = 3
    additional_pigs = 5
    additional_goats = 2
    total_cows = original_cows + additional_cows
    total_pigs = original_pigs + additional_pigs
    total_goats = original_goats + additional_goats
    total_animals = total_cows + total_pigs + total_goats
    result = total_animals

    return result

print(solution())