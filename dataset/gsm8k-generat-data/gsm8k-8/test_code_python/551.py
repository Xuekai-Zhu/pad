def solution():
    # Calculate Arlene's hiking pace without considering the weight of the backpack
    pace_without_backpack = 24 / 6

    # Convert Arlene's height to inches
    height_inches = 5 * 12

    # Calculate the number of calories burned by Arlene while hiking with the backpack
    calories_burned = 0.57 * height_inches + 0.15 * pace_without_backpack + 0.39 * 60 + 0.18 * 60 + 3.5

    # Calculate Arlene's hiking pace with the backpack
    pace_with_backpack = (24 / calories_burned) * 60

    # Convert the pace to miles per hour
    pace_mph = pace_with_backpack / 60

    result = pace_mph
    return result

print(solution())