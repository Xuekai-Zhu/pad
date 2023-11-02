def solution():
    total_flowers = 10
    red_flowers = 4
    white_flowers = 2

    # Calculate the number of blue flowers
    blue_flowers = total_flowers - red_flowers - white_flowers

    # Calculate the percentage of blue flowers
    percentage_blue = (blue_flowers / total_flowers) * 100
    result = percentage_blue
    return result

print(solution())