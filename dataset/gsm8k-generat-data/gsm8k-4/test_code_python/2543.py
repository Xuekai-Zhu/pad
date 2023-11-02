def solution():
    """Matthew drinks 4 glasses of water per day. Each glass is 5 ounces. He decides to just buy a 35 ounces water bottle. How many times will he fill it each week?"""
    # Define the amount of water Matthew drinks per day and per week
    water_per_glass = 5.0
    glasses_per_day = 4
    water_per_day = water_per_glass * glasses_per_day
    water_per_week = water_per_day * 7

    # Calculate the number of times Matthew will need to fill the water bottle per week
    fills_per_week = water_per_week / 35.0

    # Round up to the nearest integer
    fills_per_week = int(round(fills_per_week, 0))

    # Return the result
    result = fills_per_week
    return result

print(solution())