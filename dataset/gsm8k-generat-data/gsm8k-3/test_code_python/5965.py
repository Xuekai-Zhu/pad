def solution():
    """Over several years, Daniel has adopted any stray animals he sees on the side of the road.  He now has 2 horses, 5 dogs, 7 cats, 3 turtles, and 1 goat.  All of the animals are perfectly healthy.  In total, how many legs do his animals have?"""
    # Define the number of legs for each type of animal
    HORSE_LEGS = 4
    DOG_LEGS = 4
    CAT_LEGS = 4
    TURTLE_LEGS = 4
    GOAT_LEGS = 4

    # Define the number of each type of animal
    horses = 2
    dogs = 5
    cats = 7
    turtles = 3
    goats = 1

    # Calculate the total number of legs
    total_legs = (horses * HORSE_LEGS) + (dogs * DOG_LEGS) + \
                 (cats * CAT_LEGS) + (turtles * TURTLE_LEGS) + \
                 (goats * GOAT_LEGS)

    # Display the total number of legs
    result = total_legs
    return result

print(solution())