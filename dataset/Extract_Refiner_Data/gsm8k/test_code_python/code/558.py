def solution():
    
    # Define the initial angle of the pyramid
    initial_angle = 32

    # Define the sun's moving speed and the time the sun has moved
    sun_speed = 5
    sun_time = 10

    # Calculate the distance the sun will travel from the ground to Sahir's house
    sun_distance = sun_speed * sun_time

    # Calculate the distance from the ground to the sun
    sun_to_sun = sun_distance - initial_angle

    # Display the distance from the ground to the sun
    result = sun_to_sun
    return result

print(solution())