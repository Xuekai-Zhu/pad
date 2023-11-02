def solution():
    
    total_milk = 16
    kids_share = 0.75 * total_milk
    remaining_milk = total_milk - kids_share
    cooking_share = 0.5 * remaining_milk
    leftover_milk = remaining_milk - cooking_share
    result = leftover_milk
    return result

print(solution())