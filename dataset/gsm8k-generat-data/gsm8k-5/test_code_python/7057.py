def solution():
    total_flowers = 96  # There are 96 flowers in total
    green_flowers = 9  # There are 9 green flowers
    red_flowers = 3 * green_flowers  # There are three times more red flowers than green flowers
    blue_flowers = total_flowers // 2  # Blue flowers are 50% of the total flower count
    yellow_flowers = total_flowers - green_flowers - red_flowers - blue_flowers  # Calculate the number of yellow flowers

    result = yellow_flowers
    return result

print(solution())