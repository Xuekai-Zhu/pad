def solution():
    """Mark has kangaroos and goats.  Kangaroos have two legs and goats have four legs.  If he has 23 kangaroos and three times as many goats as kangaroos what is the total number of legs of all his animals?"""
    # Define the number of legs of kangaroos and goats
    KANGAROO_LEGS = 2
    GOAT_LEGS = 4

    # Define the number of kangaroos and goats
    kangaroos = 23
    goats = kangaroos * 3

    # Calculate the total number of legs
    total_legs = (kangaroos * KANGAROO_LEGS) + (goats * GOAT_LEGS)

    # Display the total number of legs
    result = total_legs
    return result

print(solution())