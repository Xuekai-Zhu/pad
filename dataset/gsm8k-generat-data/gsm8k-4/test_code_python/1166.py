def solution():
    """A gecko eats 70 crickets every three days. The first day she eats 30% of the crickets. The second day she eats 6 less than the first, and the third day she finishes up the remaining crickets. How many crickets does she eat on the third day?"""
    # Define the number of crickets the gecko eats every three days
    CRICKETS_PER_TRIP = 70

    # Calculate the number of crickets the gecko eats on the first day
    first_day = CRICKETS_PER_TRIP * 0.3

    # Calculate the number of crickets the gecko eats on the second day
    second_day = first_day - 6

    # Calculate the number of crickets the gecko eats on the third day
    third_day = CRICKETS_PER_TRIP - first_day - second_day

    result = third_day
    return result

print(solution())