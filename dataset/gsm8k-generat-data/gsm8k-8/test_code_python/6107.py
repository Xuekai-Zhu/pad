def solution():
    # Define the number of cows, sheep, and chickens
    num_cows = 4
    num_sheep = 3
    num_chickens = 7

    # Define the amount of food each animal eats per day
    cow_food = 2
    sheep_food = 2
    chicken_food = 3

    # Calculate the total amount of food needed per day
    total_food = (num_cows * cow_food) + (num_sheep * sheep_food) + (num_chickens * chicken_food)
    result = total_food
    return result

print(solution())