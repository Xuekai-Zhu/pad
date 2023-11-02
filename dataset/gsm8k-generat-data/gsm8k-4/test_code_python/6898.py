def solution():
    """John buys 3 different coolers. The first one is 100 liters. The second is 50% bigger than that and the third is half the size of the second. How much total water can they hold?"""
    # Define the size of the first cooler
    cooler1 = 100

    # Calculate the size of the second cooler, which is 50% bigger than the first
    cooler2 = cooler1 + (cooler1 * 0.5)

    # Calculate the size of the third cooler, which is half the size of the second
    cooler3 = cooler2 / 2

    # Calculate the total water the coolers can hold
    total_water = cooler1 + cooler2 + cooler3

    # return the result
    result = total_water
    return result

print(solution())