def solution():
    
    total_flowers = 12
    daisies = 2
    remaining_flowers = total_flowers - daisies
    tulips = remaining_flowers * (3/5)
    sunflowers = remaining_flowers - tulips
    result = sunflowers
    return result

print(solution())