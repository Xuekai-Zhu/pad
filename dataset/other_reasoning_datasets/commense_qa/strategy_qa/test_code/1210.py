def solution():
    # Define the locations of Disney Concert Hall, Disney Studio, and Los Angeles
    disney_concert_hall_location = "Los Angeles"
    disney_studio_location = "Los Angeles"
    los_angeles_location = "Los Angeles County"
    # Check if Disney is associated with Los Angeles County
    if disney_concert_hall_location == los_angeles_location or disney_studio_location == los_angeles_location:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())