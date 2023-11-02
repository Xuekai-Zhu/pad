def solution():
    """Over several years, Daniel has adopted any stray animals he sees on the side of the road.  He now has 2 horses, 5 dogs, 7 cats, 3 turtles, and 1 goat.  All of the animals are perfectly healthy.  In total, how many legs do his animals have?"""
    # Define the number of legs for each type of animal
    horse_legs = 4
    dog_legs = 4
    cat_legs = 4
    turtle_legs = 4
    goat_legs = 4

    # Calculate the total number of legs
    total_legs = (2 * horse_legs) + (5 * dog_legs) + (7 * cat_legs) + (3 * turtle_legs) + (1 * goat_legs)

    # return the result
    result = total_legs
    return result

print(solution())