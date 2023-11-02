def solution():
    """John buys 3 different coolers. The first one is 100 liters. The second is 50% bigger than that and the third is half the size of the second. How much total water can they hold?"""
    first_cooler = 100
    second_cooler = 1.5 * first_cooler
    third_cooler = 0.5 * second_cooler
    total_water = first_cooler + second_cooler + third_cooler
    result = total_water
    return result

print(solution())