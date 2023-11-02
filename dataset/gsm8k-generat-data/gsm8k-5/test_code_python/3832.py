def solution():
    flowers_per_color = 125  # The florist planted 125 seeds for each color of flower
    flowers = {
        'red': flowers_per_color - 45,
        'yellow': flowers_per_color - 61,
        'orange': flowers_per_color - 30,
        'purple': flowers_per_color - 40
    }  # Subtract the number of flowers killed by the fungus from the total number of flowers

    bouquets = min(flowers.values()) // 9  # Divide the minimum number of flowers by 9 to get the number of bouquets

    result = bouquets
    return result

print(solution())