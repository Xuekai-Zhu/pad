def solution():
    # Calculate the total amount of water needed to fill the glasses
    total_water_needed = 10 * 6 * (1 - 4/5)  # each glass has 6 ounces volume and is 4/5 full, so 1 - 4/5 = 1/5 is the amount of water needed to fill it
    result = total_water_needed
    return result

print(solution())