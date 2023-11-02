def solution():
    """During one day, there are 4 boat trips through the lake. The boat can take up to 12 people during one trip. How many people can the boat transport in 2 days?"""
    # Define the boat capacity and the number of trips per day
    BOAT_CAPACITY = 12
    TRIPS_PER_DAY = 4

    # Calculate the total number of people the boat can transport in one day
    total_people_per_day = BOAT_CAPACITY * TRIPS_PER_DAY

    # Calculate the total number of people the boat can transport in two days
    total_people_in_two_days = total_people_per_day * 2

    # Return the result
    result = total_people_in_two_days
    return result

print(solution())