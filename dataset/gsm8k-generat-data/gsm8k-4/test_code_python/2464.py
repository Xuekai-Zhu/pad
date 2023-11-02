def solution():
    """A mother is making her own bubble mix out of dish soap and water for her two-year-old son. The recipe she is following calls for 3 tablespoons of soap for every 1 cup of water. If the container she hopes to store the bubble mix in can hold 40 ounces of liquid, and there are 8 ounces in a cup of water, how many tablespoons of soap should she add to the container (assuming that the soap itself doesn't count towards the capacity of the container)?"""
    # Define the ratio of soap to water in the bubble mix
    soap_to_water_ratio = 3 / 8

    # Calculate the amount of water needed to fill the container
    water_in_ounces = 40

    # Convert the amount of water to cups
    water_in_cups = water_in_ounces / 8

    # Calculate the amount of soap needed for the bubble mix
    soap_in_tablespoons = soap_to_water_ratio * water_in_cups

    result = soap_in_tablespoons
    return result

print(solution())