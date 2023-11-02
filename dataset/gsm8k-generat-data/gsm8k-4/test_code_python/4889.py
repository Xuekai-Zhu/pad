def solution():
    """Peter has 15 birds. 1/3 are ducks. The rest are chickens and require special feed that costs $2 per bird. How much does it cost to feed the chickens?"""
    # Define the total number of birds and the fraction that are ducks
    total_birds = 15
    duck_fraction = 1/3

    # Calculate the number of ducks and chickens
    duck_count = int(total_birds * duck_fraction)
    chicken_count = total_birds - duck_count

    # Calculate the cost to feed the chickens
    chicken_cost = chicken_count * 2

    result = chicken_cost
    return result

print(solution())