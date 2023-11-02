def solution():
    """John drinks 2 energy drinks. 1 of them is a 12-ounce drink with 250 grams of caffeine.
    The second drink is 3 times more caffeinated per ounce but only 2 ounces.
    He then takes a caffeine pill that has as much caffeine as his 2 drinks combined. How much caffeine did he consume?"""
    drink1_ounces = 12
    drink1_caffeine = 250
    drink2_ounces = 2
    drink2_caffeine_per_ounce = 3 * drink1_caffeine / drink1_ounces
    drink2_caffeine = drink2_caffeine_per_ounce * drink2_ounces
    total_caffeine = drink1_caffeine + drink2_caffeine
    caffeine_pill = total_caffeine
    total_caffeine += caffeine_pill
    result = total_caffeine
    return result

print(solution())