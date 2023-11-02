def solution():
    # Calculate the total number of remaining flowers
    red_flowers = 125 - 45
    yellow_flowers = 125 - 61
    orange_flowers = 125 - 30
    purple_flowers = 125 - 40

    # Calculate the total number of bouquets that can be made
    total_bouquets = min(red_flowers, yellow_flowers, orange_flowers, purple_flowers) // 9
    result = total_bouquets
    return result

print(solution())