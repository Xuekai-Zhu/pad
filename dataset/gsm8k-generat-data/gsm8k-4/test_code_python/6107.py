def solution():
    """Dany owns a farm, in his farm he has 4 cows and 3 sheep that eat 2 bushels a day. He also has 7 chickens that eat 3 bushels a day. How many bushels should he have to suffice the animals for a day?"""
    # Define the number of cows, sheep, and chickens
    cows = 4
    sheep = 3
    chickens = 7

    # Define the amount of food each animal needs per day
    cow_food = 2
    sheep_food = 2
    chicken_food = 3

    # Calculate the total amount of food needed for all animals per day
    total_food = (cows * cow_food) + (sheep * sheep_food) + (chickens * chicken_food)

    # Return the result
    result = total_food
    return result

print(solution())