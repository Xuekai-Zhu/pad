def solution():
    """Ivy drinks 2.5 liters of water each day. How many bottles of 2-liter water should Ivy buy for her 4 days consumption?"""
    # Define the amount of water Ivy drinks in 4 days
    total_water = 2.5 * 4

    # Calculate the number of 2-liter bottles needed
    bottles_needed = total_water / 2

    # Round up to the nearest whole number
    bottles_needed = int(bottles_needed) + 1

    result = bottles_needed
    return result

print(solution())