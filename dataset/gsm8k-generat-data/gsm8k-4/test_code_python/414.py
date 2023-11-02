def solution():
    """John drinks 2 energy drinks. 1 of them is a 12-ounce drink with 250 grams of caffeine. The second drink is 3 times more caffeinated per ounce but only 2 ounces. He then takes a caffeine pill that has as much caffeine as his 2 drinks combined. How much caffeine did he consume?"""
    # Calculate the caffeine in the first drink
    caffeine_1 = 250

    # Calculate the caffeine per ounce in the second drink
    caffeine_per_ounce = caffeine_1 / 12 * 3

    # Calculate the caffeine in the second drink
    caffeine_2 = caffeine_per_ounce * 2

    # Calculate the total caffeine consumed
    total_caffeine = caffeine_1 + caffeine_2

    # Return the result
    result = total_caffeine
    return result

print(solution())