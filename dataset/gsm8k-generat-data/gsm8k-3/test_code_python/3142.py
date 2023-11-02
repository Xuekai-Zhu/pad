def solution():
    """Three-quarters of the oil from a 4000-liter tank (that was initially full) was poured into a 20000-liter capacity tanker that already had 3000 liters of oil. How many more liters of oil would be needed to make the large tanker half-full?"""
    # Calculate the amount of oil in the first tank that was poured into the second tank
    transferred_oil = 0.75 * 4000

    # Calculate the current amount of oil in the second tank
    current_oil = transferred_oil + 3000

    # Calculate the amount of oil needed to fill the second tank halfway
    half_full = 0.5 * 20000
    needed_oil = half_full - current_oil

    # Display the amount of oil needed
    result = needed_oil
    return result

print(solution())