def solution():
    """In the park, the first rose bush has 12 red flowers. The second rose bush has 18 pink flowers. The third rose bush has 20 yellow flowers. The fourth rose bush has 8 orange flowers. For her vase, Lorelei picks 50% of the red roses, 50% pink roses, 25% of the yellow roses, and 25% orange roses. How many roses are in her vase?"""
    red_flowers = 12
    pink_flowers = 18
    yellow_flowers = 20
    orange_flowers = 8
    total_red_flowers = 0.5 * red_flowers
    total_pink_flowers = 0.5 * pink_flowers
    total_yellow_flowers = 0.25 * yellow_flowers
    total_orange_flowers = 0.25 * orange_flowers
    total_flowers = total_red_flowers + total_pink_flowers + total_yellow_flowers + total_orange_flowers
    result = total_flowers
    return result

print(solution())