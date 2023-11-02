def solution():
    # Calculate the number of cups of lemonade in the pitcher
    drink_ratio = 1 / (1/4 + 1 + 1/4)  # the ratio of lemonade to the total drink
    lemonade_cups = drink_ratio * 18  # the number of cups of lemonade in the pitcher
    result = lemonade_cups
    return result

print(solution())