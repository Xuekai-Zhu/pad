def solution():
    # Calculate the total amount of water Remi drinks in a week
    total_refills = 3 * 7  # Remi refills the bottle 3 times a day for 7 days
    total_water = (20 * total_refills) - 5 - 8 # Remi spills 5 ounces the first time and 8 ounces the second time
    result = total_water
    return result

print(solution())