def solution():
    """John drinks 2 energy drinks. 1 of them is a 12-ounce drink with 250 grams of caffeine. The second drink is 3 times more caffeinated per ounce but only 2 ounces. He then takes a caffeine pill that has as much caffeine as his 2 drinks combined. How much caffeine did he consume?"""
    drink1_caffeine = 250
    drink1_size = 12
    drink2_caffeine_per_ounce = drink1_caffeine * 3
    drink2_size = 2
    drink2_caffeine = drink2_caffeine_per_ounce * drink2_size
    pill_caffeine = (drink1_caffeine + drink2_caffeine)
    total_caffeine = drink1_caffeine + drink2_caffeine + pill_caffeine
    result = total_caffeine
    
    return result

print(solution())