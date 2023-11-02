def solution():
    
    cherry_sweets = 30
    strawberry_sweets = 40
    pineapple_sweets = 50
    aaron_eats = 0.5
    cherry_sweets_left = (1 - aaron_eats) * cherry_sweets - 5
    strawberry_sweets_left = (1 - aaron_eats) * strawberry_sweets
    pineapple_sweets_left = (1 - aaron_eats) * pineapple_sweets
    total_sweets_left = cherry_sweets_left + strawberry_sweets_left + pineapple_sweets_left
    result = total_sweets_left
    return result

print(solution())