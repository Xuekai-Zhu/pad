def solution():
    """John buys 3 different coolers.  The first one is 100 liters.  The second is 50% bigger than that and the third is half the size of the second.  How much total water can they hold?"""
    # Define the size of the first cooler
    cooler1 = 100

    # Calculate the size of the second cooler
    cooler2 = cooler1 * 1.5

    # Calculate the size of the third cooler
    cooler3 = cooler2 * 0.5

    # Calculate the total water that can be held
    total_size = cooler1 + cooler2 + cooler3

    # Display the total size
    result = total_size
    return result

print(solution())