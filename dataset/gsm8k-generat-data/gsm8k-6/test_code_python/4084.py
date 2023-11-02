def solution():
    total_flowers = 12  # one dozen flowers
    daisies = 2
    remaining_flowers = total_flowers - daisies
    tulips = (3/5) * remaining_flowers
    sunflowers = remaining_flowers - tulips
    result = sunflowers
    return result

print(solution())