def solution():
    """Dany owns a farm, in his farm he has 4 cows and 3 sheep that eat 2 bushels a day. He also has 7 chickens that eat 3 bushels a day. How many bushels should he have to suffice the animals for a day?"""
    # Define the number of animals and their food requirements
    COWS = 4
    SHEEP = 3
    CHICKENS = 7
    COW_FOOD = 2
    SHEEP_FOOD = 2
    CHICKEN_FOOD = 3

    # Calculate the total food requirements for all the animals
    total_food = (COWS * COW_FOOD) + (SHEEP * SHEEP_FOOD) + (CHICKENS * CHICKEN_FOOD)

    # Display the total food requirements
    result = total_food
    return result

print(solution())