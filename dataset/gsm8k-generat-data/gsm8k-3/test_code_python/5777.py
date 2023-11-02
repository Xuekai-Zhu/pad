def solution():
    """For the family reunion, Peter is buying 16 pounds of bone-in chicken and half that amount in hamburgers.  He's going to buy 2 more pounds of hot dogs than hamburgers.  He's also going to buy several sides that will weigh half the amount of hot dogs.  How many pounds of food will he buy?"""
    # Calculate the amount of hamburgers
    hamburgers = 16 / 2

    # Calculate the amount of hot dogs
    hot_dogs = hamburgers + 2

    # Calculate the amount of sides
    sides = hot_dogs / 2

    # Calculate the total amount of food
    total_food = 16 + hamburgers + hot_dogs + sides

    # Display the total amount of food
    result = total_food
    return result

print(solution())