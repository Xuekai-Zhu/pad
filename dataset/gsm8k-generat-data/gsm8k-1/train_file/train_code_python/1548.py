def solution():
    """Melanie does her weekly shopping at the farmer's market. She starts with an 8-ounce wheel of brie cheese. Next is a 1 pound loaf of bread. She grabs a pound of tomatoes and 2 pounds of zucchini. After that, she grabs 1 1/2 pounds of chicken breasts and treats herself to 8 ounces of fresh raspberries and 8 ounces of fresh blueberries. How many pounds of food does she buy?"""
    brie_weight = 0.5  # 8 ounces is half a pound
    bread_weight = 1
    tomato_weight = 1
    zucchini_weight = 2
    chicken_weight = 1.5
    raspberry_weight = 0.5  # 8 ounces is half a pound
    blueberry_weight = 0.5  # 8 ounces is half a pound
    
    total_weight = (
        brie_weight + bread_weight + tomato_weight + zucchini_weight +
        chicken_weight + raspberry_weight + blueberry_weight
    )
    result = total_weight
    return result

print(solution())