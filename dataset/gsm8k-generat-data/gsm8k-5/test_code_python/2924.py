def solution():
    total_flowers = 10  # Madeline has 10 flowers
    red_flowers = 4  # 4 flowers are red
    white_flowers = 2  # 2 flowers are white

    # Calculate the number of blue flowers
    blue_flowers = total_flowers - red_flowers - white_flowers

    # Calculate the percentage of blue flowers
    blue_percentage = (blue_flowers / total_flowers) * 100
    result = blue_percentage
    return result

print(solution())