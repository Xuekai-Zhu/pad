def solution():
    """
    Melanie does her weekly shopping at the farmer's market. 
    She starts with an 8-ounce wheel of brie cheese. Next is a 1 pound loaf of bread. 
    She grabs a pound of tomatoes and 2 pounds of zucchini. 
    After that, she grabs 1 1/2 pounds of chicken breasts and treats herself to 8 ounces of fresh raspberries and 8 ounces of fresh blueberries. 
    How many pounds of food does she buy?
    """
    # Define the initial weight of the brie cheese in pounds
    brie_weight = 0.5

    # Define the weight of the bread in pounds
    bread_weight = 1.0

    # Define the weight of the tomatoes in pounds
    tomatoes_weight = 1.0

    # Define the weight of the zucchini in pounds
    zucchini_weight = 2.0

    # Define the weight of the chicken breasts in pounds
    chicken_weight = 1.5

    # Define the weight of the raspberries in pounds
    raspberries_weight = 0.5

    # Define the weight of the blueberries in pounds
    blueberries_weight = 0.5

    # Calculate the total weight in pounds
    total_weight = (brie_weight + bread_weight + tomatoes_weight + zucchini_weight +
                    chicken_weight + raspberries_weight + blueberries_weight)

    # return the result
    result = total_weight
    return result

print(solution())