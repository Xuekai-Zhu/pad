def solution():
    # Size of the first cooler
    cooler1 = 100

    # Size of the second cooler, which is 50% bigger than the first cooler
    cooler2 = cooler1 * 1.5

    # Size of the third cooler, which is half the size of the second cooler
    cooler3 = cooler2 / 2

    # Total water the coolers can hold
    total_water = cooler1 + cooler2 + cooler3
    result = total_water
    return result

print(solution())