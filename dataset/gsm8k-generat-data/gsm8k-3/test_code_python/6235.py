def solution():
    """Samson is going to another town which is 140 km away. He will use his car that uses ten liters of gasoline for a distance of 70 km. How many liters of gasoline will Samson need for a one-way trip?"""
    # Define the distance Samson will travel
    distance = 140

    # Define the distance Samson's car can travel with 1 liter of gasoline
    car_distance = 70 / 10

    # Calculate the amount of gasoline Samson will need for a one-way trip
    gas_needed = distance / car_distance

    # Display the amount of gasoline needed
    result = gas_needed
    return result

print(solution())