def solution():
    """In January the families visiting a national park see animals 26 times. In February 
    the families that visit the national park see animals three times as many as were seen 
    there in January. Then in March the animals are shyer and the families who visit the 
    national park see animals half as many times as they were seen in February. 
    How many times total did families see an animal in the first three months of the year?"""
    # Define the number of animal sightings in January
    jan_sightings = 26

    # Calculate the number of animal sightings in February
    feb_sightings = jan_sightings * 3

    # Calculate the number of animal sightings in March
    mar_sightings = feb_sightings / 2

    # Calculate the total number of animal sightings in the first three months
    total_sightings = jan_sightings + feb_sightings + mar_sightings

    # Display the total number of animal sightings
    result = total_sightings
    return result

print(solution())