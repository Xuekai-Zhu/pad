def solution():
    # Calculate the total time to clean the bedrooms
    time_bedrooms = 3 * 20  # Each bedroom takes 20 minutes to clean

    # Calculate the time to clean the living room
    time_living_room = time_bedrooms * 3  # The living room takes as long as the 3 bedrooms combined

    # Calculate the time to clean the bathrooms
    time_bathrooms = time_living_room * 2  # The bathroom takes twice as long as the living room

    # Calculate the total time to clean the house
    time_house = time_bedrooms + time_living_room + time_bathrooms

    # Calculate the time to clean the outside
    time_outside = time_house * 2  # The outside takes twice as long as cleaning the house

    # Calculate the total time James and his siblings work
    total_time = (time_house + time_outside) / 60  # Convert minutes to hours
    result = total_time
    return result

print(solution())