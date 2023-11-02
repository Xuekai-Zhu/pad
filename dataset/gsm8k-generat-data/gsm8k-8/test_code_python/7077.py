def solution():
    # Convert 8 inches to feet
    additional_snow = 8/12 

    # Calculate the snow total after the second day
    snow_total = 0.5 + additional_snow 

    # Convert 2 inches of melted snow to feet
    melted_snow = 2/12 

    # Calculate the snow total after the fourth day
    snow_total -= melted_snow 

    # Calculate the amount of snow received on the fifth day
    snow_received = 2 * 0.5 

    # Add the snow received on the fifth day to the snow total
    snow_total += snow_received 

    result = snow_total
    return result

print(solution())