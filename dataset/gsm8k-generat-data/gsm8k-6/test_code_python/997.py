def solution():
    # Each person gets equal share of fish
    fish_per_person = 1/3
    total_fish = 3  # Ittymangnark catches enough fish for three of them

    # Calculate the number of fish eyes per fish
    fish_eye_ratio = 2/100  # Oomyapeck gives two eyes to his dog and eats the rest

    # Calculate the number of fish Oomyapeck eats
    eaten_fish_eyes = 22
    eaten_fish = eaten_fish_eyes / fish_eye_ratio

    # Calculate the remaining fish to be split among Ittymangnark and Kingnook
    remaining_fish = total_fish - eaten_fish

    # Calculate the number of fish each of them will be given to eat
    fish_per_person_after_Oomyapeck = remaining_fish * fish_per_person
    result = fish_per_person_after_Oomyapeck
    return result

print(solution())