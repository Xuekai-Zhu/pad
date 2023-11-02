def solution():
    sister_height_in_inches = 51 # 4 feet and 3 inches is 51 inches
    sunflower_height_in_inches = sister_height_in_inches + 21  # Marissa's sunflower is 21 inches taller than her sister
    sunflower_height_in_feet = sunflower_height_in_inches / 12  # Convert height in inches to feet

    result = sunflower_height_in_feet
    return result

print(solution())