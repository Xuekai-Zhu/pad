def solution():
    sister_height_inches = 51  # 4 feet 3 inches = 51 inches
    sunflower_height_inches = sister_height_inches + 21

    # Convert sunflower height from inches to feet
    sunflower_height_feet = sunflower_height_inches / 12
    
    result = sunflower_height_feet
    return result

print(solution())