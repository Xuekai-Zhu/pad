def solution():
    # Convert 8 inches of snow to feet
    additional_snow_day_two = 8 / 12

    # Convert 2 inches of melted snow to feet
    melted_snow = 2 / 12

    # Calculate the total snow after the first two days
    total_snow_day_two = 0.5 + additional_snow_day_two - melted_snow

    # Calculate the snow on the fifth day
    snow_day_five = 2 * 0.5

    # Calculate the total snow after five days
    total_snow_day_five = total_snow_day_two + snow_day_five

    result = total_snow_day_five
    return result

print(solution())