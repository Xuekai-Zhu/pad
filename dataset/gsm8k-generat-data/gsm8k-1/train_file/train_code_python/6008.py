def solution():
    """In the park, the first rose bush has 12 red flowers. The second rose bush has 18 pink flowers. The third rose bush has 20 yellow flowers. The fourth rose bush has 8 orange flowers. For her vase, Lorelei picks 50% of the red roses, 50% pink roses, 25% of the yellow roses, and 25% orange roses. How many roses are in her vase?"""
    red_roses = 12
    pink_roses = 18
    yellow_roses = 20
    orange_roses = 8
    
    vase_red_roses = red_roses * 0.5
    vase_pink_roses = pink_roses * 0.5
    vase_yellow_roses = yellow_roses * 0.25
    vase_orange_roses = orange_roses * 0.25
    
    total_roses = vase_red_roses + vase_pink_roses + vase_yellow_roses + vase_orange_roses
    result = total_roses
    return result

print(solution())