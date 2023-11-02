def solution():
    # Define the number of eyes per fish
    eyes_per_fish = 2/3

    # Calculate the number of fish needed for Oomyapeck to eat 22 eyes
    fish_for_eyes = 22 / eyes_per_fish

    # Calculate the total number of fish caught by Ittymangnark
    total_fish = fish_for_eyes / (2/3 + 1)

    # Calculate the number of fish each person gets to eat
    fish_per_person = total_fish / 3

    result = fish_per_person
    return result

print(solution())