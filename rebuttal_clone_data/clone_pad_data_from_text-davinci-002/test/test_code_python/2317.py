def solution():
    total_flowers = 12
    daisies = 2
    tulips = (total_flowers - daisies) * (3/5)
    sunflowers = total_flowers - daisies - tulips
    result = sunflowers
    return result

print(solution())