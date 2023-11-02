def solution():
    # Each day, Ittymangnark catches enough fish for the three of them to eat for the day
    # They split the fish equally between the three of them
    total_fish = 3

    # After they have split the fish, they give Oomyapeck all of the eyes
    # Oomyapeck gives two of the eyes to his dog and eats the rest himself
    total_eyes = 22 + 2

    # Each fish has 2 eyes, so the total number of fish is the number of eyes divided by 2
    total_fish += total_eyes / 2

    # Divide the total number of fish by 3 to get the number of fish each of them will be given to eat
    fish_per_person = total_fish / 3
    result = fish_per_person
    return result

print(solution())