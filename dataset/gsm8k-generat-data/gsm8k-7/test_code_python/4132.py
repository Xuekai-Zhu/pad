def solution():
    height_1 = 2
    height_2 = height_1 * 1.5
    height_3 = height_2 * 1.5
    height_4 = height_3 * 2
    height_5 = height_4 * 0.5

    # Calculate the total height of the tree at 5 years old
    total_height = height_1 + height_2 + height_3 + height_4 + height_5
    result = total_height
    return result

print(solution())