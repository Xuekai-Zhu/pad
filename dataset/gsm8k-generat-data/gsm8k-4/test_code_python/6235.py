def solution():
    """Samson is going to another town which is 140 km away. He will use his car that uses ten liters of gasoline for a distance of 70 km. How many liters of gasoline will Samson need for a one-way trip?"""
    # Calculate the liters of gasoline needed for one kilometer
    gasoline_per_km = 10 / 70

    # Calculate the liters of gasoline needed for the entire trip
    gasoline_needed = gasoline_per_km * 140

    # Return the result
    result = gasoline_needed
    return result

print(solution())