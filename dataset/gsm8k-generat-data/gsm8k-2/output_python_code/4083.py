def solution():
    """Rose bought her mother one dozen flowers. Two of the flowers are daisies. Three-fifths of the remaining flowers are tulips and the rest are sunflowers. How many sunflowers are there?"""
    total_flowers = 12
    daisies = 2
    remaining_flowers = total_flowers - daisies
    tulips = (3/5) * remaining_flowers
    sunflowers = remaining_flowers - tulips
    result = sunflowers
    return result

print(solution())