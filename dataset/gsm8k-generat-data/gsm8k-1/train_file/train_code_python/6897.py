def solution():
    """John buys 3 different coolers. The first one is 100 liters. The second is 50% bigger than that and the third is half the size of the second. How much total water can they hold?"""
    cooler1 = 100
    cooler2 = cooler1 * 1.5
    cooler3 = cooler2 * 0.5
    total_water = cooler1 + cooler2 + cooler3
    result = total_water
    return result

print(solution())