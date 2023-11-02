def solution():
    # Define initial variables
    starting_goldfish = 18
    goldfish_die_per_week = 5
    goldfish_added_per_week = 3

    # Calculate the number of goldfish left after 7 weeks
    goldfish_left = starting_goldfish - (goldfish_die_per_week * 7)
    goldfish_left += (goldfish_added_per_week * 7)

    result = goldfish_left
    return result

print(solution())