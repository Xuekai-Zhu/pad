def solution():
    # Calculate the total amount of caffeine John consumed
    caffeine_first_drink = 250  # in grams
    caffeine_second_drink = 3 * (12/2) * 28.35  # 3 times more caffeinated per ounce than first drink, but only 2 ounces; converted to grams
    total_caffeine = caffeine_first_drink + caffeine_second_drink  # in grams
    caffeine_pill = total_caffeine  # caffeine pill has as much caffeine as both drinks combined
    total_consumed = total_caffeine + caffeine_pill  # in grams
    result = total_consumed
    return result

print(solution())