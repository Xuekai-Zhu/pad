def solution():
    # Find the number of red and yellow flowers
    red_flowers = 2 * 10
    yellow_flowers = red_flowers - 5

    # Find the total number of purple and pink flowers combined
    purple_pink = 105 - 10 - red_flowers - yellow_flowers

    # Divide them equally between purple and pink
    result = purple_pink / 2
    return result

print(solution())