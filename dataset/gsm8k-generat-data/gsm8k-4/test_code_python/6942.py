def solution():
    """Mark has kangaroos and goats. Kangaroos have two legs and goats have four legs. If he has 23 kangaroos and three times as many goats as kangaroos what is the total number of legs of all his animals?"""
    # Define the number of kangaroos
    kangaroos = 23

    # Calculate the number of goats
    goats = 3 * kangaroos

    # Calculate the total number of legs
    total_legs = (kangaroos * 2) + (goats * 4)

    result = total_legs
    return result

print(solution())