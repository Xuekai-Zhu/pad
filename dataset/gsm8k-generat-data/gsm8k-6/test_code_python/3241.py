def solution():
    # Calculate the number of good fish James has after 20% have gone bad
    good_fish = 400 * 0.8  # 20% of the fish have gone bad

    # Calculate the number of sushi rolls James can make with the remaining good fish
    sushi_rolls = good_fish // 40

    result = sushi_rolls
    return result

print(solution())