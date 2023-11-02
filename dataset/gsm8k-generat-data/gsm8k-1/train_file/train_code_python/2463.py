def solution():
    """A mother is making her own bubble mix out of dish soap and water for her two-year-old son. The recipe she is following calls for 3 tablespoons of soap for every 1 cup of water. If the container she hopes to store the bubble mix in can hold 40 ounces of liquid, and there are 8 ounces in a cup of water, how many tablespoons of soap should she add to the container (assuming that the soap itself doesn't count towards the capacity of the container)?"""
    soap_per_water = 3/8
    capacity_cups = 40/8
    soap_needed = soap_per_water * capacity_cups
    result = soap_needed
    return result

print(solution())