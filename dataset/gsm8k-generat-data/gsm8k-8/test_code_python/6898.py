def solution():
    # Define the size of the first cooler
    cooler1_size = 100

    # Calculate the size of the second cooler
    cooler2_size = cooler1_size * 1.5

    # Calculate the size of the third cooler
    cooler3_size = cooler2_size / 2

    # Calculate the total size of all three coolers
    total_size = cooler1_size + cooler2_size + cooler3_size

    # Assume each cooler is filled to 80% capacity, calculate the total water they can hold
    total_water = total_size * 0.8

    result = total_water
    return result

print(solution())