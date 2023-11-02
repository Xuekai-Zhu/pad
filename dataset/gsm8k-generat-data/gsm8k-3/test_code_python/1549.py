def solution():
    """Melanie does her weekly shopping at the farmer's market.  She starts with an 8-ounce wheel of brie cheese.  Next is a 1 pound loaf of bread.  She grabs a pound of tomatoes and 2 pounds of zucchini.  After that, she grabs 1 1/2 pounds of chicken breasts and treats herself to 8 ounces of fresh raspberries and 8 ounces of fresh blueberries.  How many pounds of food does she buy?"""
    # Define the weight of each item in pounds
    BRIE_WEIGHT = 0.5
    BREAD_WEIGHT = 1
    TOMATO_WEIGHT = 1
    ZUCCHINI_WEIGHT = 2
    CHICKEN_WEIGHT = 1.5
    RASPBERRY_WEIGHT = 0.5
    BLUEBERRY_WEIGHT = 0.5

    # Calculate the total weight of the items Melanie bought
    total_weight = BRIE_WEIGHT + BREAD_WEIGHT + TOMATO_WEIGHT + ZUCCHINI_WEIGHT + CHICKEN_WEIGHT + RASPBERRY_WEIGHT + BLUEBERRY_WEIGHT

    # Display the total weight
    result = total_weight
    return result

print(solution())