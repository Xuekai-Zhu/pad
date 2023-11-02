def solution():
    # Caffeine in the first drink
    caffeine_first_drink = 250  # 250 grams of caffeine in a 12-ounce drink

    # Caffeine in the second drink
    caffeine_second_drink = 3 * (12 * 2)  # The second drink is 3 times more caffeinated per ounce, but only 2 ounces

    # Total caffeine in the drinks
    total_caffeine_drinks = caffeine_first_drink + caffeine_second_drink

    # Caffeine in the caffeine pill
    caffeine_pill = total_caffeine_drinks

    # Total caffeine consumed
    total_caffeine = total_caffeine_drinks + caffeine_pill
    result = total_caffeine
    return result

print(solution())