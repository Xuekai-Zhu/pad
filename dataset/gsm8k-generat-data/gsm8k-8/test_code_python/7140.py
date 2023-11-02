def solution():
    # Convert sister's height to inches
    sister_height_inches = 4 * 12 + 3

    # Calculate sunflower's height in inches
    sunflower_height_inches = sister_height_inches + 21

    # Convert sunflower's height to feet
    sunflower_height_feet = sunflower_height_inches / 12

    result = sunflower_height_feet
    return result

print(solution())