def solution():
    """Boston had .5 feet of snow on the first day of winter.  The next day they got an additional 8 inches.  Over the next 2 days, 2 inches of the snow melted.  On the fifth day, they received another 2 times the amount of snow they received on the first day.  How many feet of snow do they now have?"""
    # Define the amount of snow on the first day
    snow_1 = 0.5

    # Convert the additional snowfall on the second day from inches to feet
    snow_2 = 8 / 12

    # Calculate the amount of snow that melted over the next two days
    melted_snow = 2 / 12

    # Calculate the amount of snow on the fourth day
    snow_4 = snow_1 + snow_2 - melted_snow

    # Calculate the additional snowfall on the fifth day
    snow_5 = snow_1 * 2

    # Calculate the total amount of snow on the fifth day
    total_snow = snow_4 + snow_5

    # Display the total amount of snow
    result = total_snow
    return result

print(solution())