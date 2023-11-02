def solution():
    # Calculate the number of green M&Ms left after eating 12
    green_left = 20 - 12

    # Calculate the number of red M&Ms left after his sister eats half and adds 14 yellow
    red_left = (20 / 2) - 14

    # Calculate the total number of M&Ms left
    total_left = green_left + red_left + 14

    # Calculate the percentage chance of picking a green M&M
    green_chance = (green_left / total_left) * 100
    result = green_chance
    return result

print(solution())