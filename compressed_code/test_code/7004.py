def solution():
    
    brie_weight = 0.5  
    bread_weight = 1
    tomato_weight = 1
    zucchini_weight = 2
    chicken_weight = 1.5
    raspberry_weight = 0.5  
    blueberry_weight = 0.5  
    
    total_weight = (
        brie_weight + bread_weight + tomato_weight + zucchini_weight +
        chicken_weight + raspberry_weight + blueberry_weight
    )
    result = total_weight
    return result

print(solution())