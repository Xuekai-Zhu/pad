def solution():
    
    dozens_bought = 3
    free_flowers_per_dozen = 2
    flowers_per_dozen = 12
    total_flowers = (dozens_bought * flowers_per_dozen) + (dozens_bought * free_flowers_per_dozen)
    result = total_flowers
    return result

print(solution())