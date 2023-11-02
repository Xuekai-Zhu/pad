def solution():
    number_of_babies = 6
    number_of_worms_per_baby = 3
    number_of_worms_caught_by_papa = 9
    number_of_worms_caught_by_mama = 13
    number_of_worms_stolen = 2
    number_of_worms_needed = number_of_babies * number_of_worms_per_baby * days_needed
    number_of_worms_available = number_of_worms_caught_by_mama + number_of_worms_caught_by_papa - number_of_worms_stolen
    number_of_worms_missing = number_of_worms_needed - number_of_worms_available
    result = number_of_worms_missing
    return result

print(solution())