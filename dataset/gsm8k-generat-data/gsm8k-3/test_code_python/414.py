def solution():
    """John drinks 2 energy drinks. 1 of them is a 12-ounce drink with 250 grams of caffeine.  The second drink is 3 times more caffeinated per ounce but only 2 ounces.  He then takes a caffeine pill that has as much caffeine as his 2 drinks combined.  How much caffeine did he consume?"""
    # Calculate the total caffeine in the first drink
    drink1_caffeine = 250

    # Calculate the caffeine per ounce in the second drink
    drink2_caffeine_per_ounce = 3 * drink1_caffeine / 1  # 1 ounce in drink 2 has 3 times more caffeine than 1 ounce in drink 1

    # Calculate the total caffeine in the second drink
    drink2_caffeine = drink2_caffeine_per_ounce * 2  # drink 2 is 2 ounces

    # Calculate the total caffeine in the two drinks combined
    total_caffeine_drinks = drink1_caffeine + drink2_caffeine

    # Calculate the caffeine in the caffeine pill
    caffeine_pill_caffeine = total_caffeine_drinks

    # Calculate the total caffeine consumed
    total_caffeine = total_caffeine_drinks + caffeine_pill_caffeine

    # Display the total caffeine consumed
    result = total_caffeine
    return result

print(solution())