def solution():
    # Calculate the number of bees that constitute a fourth of the initial number
    fourth_of_initial = 80000 / 4

    # Calculate the number of days until the colony reaches a fourth of its initial number
    days_to_reach_fourth = (80000 - fourth_of_initial) / 1200
    result = days_to_reach_fourth
    return result

print(solution())