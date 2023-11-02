def solution():
    """The temperature in New York in June 2020 was 80 degrees. If the temperature in Miami on this day was 10 degrees hotter than the temperature in New York, and 25 degrees cooler than the temperature in San Diego, what was the average temperature for the three cities?"""
    # Define the temperature in New York
    NY_TEMP = 80

    # Calculate the temperature in Miami
    MIAMI_TEMP = NY_TEMP + 10

    # Calculate the temperature in San Diego
    SD_TEMP = MIAMI_TEMP + 25

    # Calculate the average temperature
    avg_temp = (NY_TEMP + MIAMI_TEMP + SD_TEMP) / 3

    # Display the average temperature
    result = avg_temp
    return result

print(solution())