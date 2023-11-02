def solution():
    """Rollo has 3 guinea pigs, the first guinea pig eats 2 cups of food, the second guinea pig eats twice as much as the first one, and the third guinea pig eats 3 cups more than the second one. How many cups of food does Rollo need to feed all his Guinea pigs?"""
    # Define the amount of food each guinea pig eats
    guinea_pig1 = 2
    guinea_pig2 = 2 * guinea_pig1
    guinea_pig3 = guinea_pig2 + 3

    # Calculate the total amount of food needed
    total_food = guinea_pig1 + guinea_pig2 + guinea_pig3

    result = total_food
    return result

print(solution())