def solution():
    """A gecko eats 70 crickets every three days. The first day she eats 30% of the crickets. The second day she eats 6 less than the first, and the third day she finishes up the remaining crickets. How many crickets does she eat on the third day?"""
    # Define the initial number of crickets
    starting_crickets = 70

    # Calculate the number of crickets eaten on the first day
    first_day_crickets = int(starting_crickets * 0.3)

    # Calculate the number of crickets eaten on the second day
    second_day_crickets = first_day_crickets - 6

    # Calculate the number of crickets remaining
    remaining_crickets = starting_crickets - first_day_crickets - second_day_crickets

    # Return the number of crickets eaten on the third day
    result = remaining_crickets
    return result

print(solution())