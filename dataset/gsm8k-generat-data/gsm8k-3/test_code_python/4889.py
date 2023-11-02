def solution():
    """Peter has 15 birds. 1/3 are ducks. The rest are chickens and require special feed that costs $2 per bird. How much does it cost to feed the chickens?"""
    # Define the number of birds and the proportion of ducks
    birds = 15
    duck_proportion = 1 / 3

    # Calculate the number of ducks and chickens
    num_ducks = round(birds * duck_proportion)
    num_chickens = birds - num_ducks

    # Calculate the cost to feed the chickens
    chicken_cost = num_chickens * 2

    # Display the cost to feed the chickens
    result = chicken_cost
    return result

print(solution())