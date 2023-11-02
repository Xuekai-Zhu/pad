def solution():
    # Calculate the size of the second cooler
    second_cooler = 1.5 * 100  # 50% bigger than the first cooler

    # Calculate the size of the third cooler
    third_cooler = 0.5 * second_cooler  # half the size of the second cooler

    # Calculate the total amount of water the coolers can hold
    total_water = 100 + second_cooler + third_cooler

    result = total_water
    return result

print(solution())