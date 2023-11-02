def solution():
    total_flowers = 12  # Rose bought one dozen flowers
    daisies = 2  # Two of the flowers are daisies
    remaining_flowers = total_flowers - daisies  # Calculate how many flowers are left

    # Calculate how many tulips there are
    tulips = int((3/5) * remaining_flowers)

    # Calculate how many sunflowers there are
    sunflowers = remaining_flowers - tulips
    result = sunflowers
    return result

print(solution())