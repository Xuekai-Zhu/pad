def solution():
    
    # Define the initial burning speed and the time burned
    initial_burning_speed = 2  # centimeters per hour
    burning_time = 1.5  # hours

    # Calculate the initial burning distance
    initial_burning_distance = initial_burning_speed * burning_time

    # Calculate the final burning distance
    final_burning_distance = initial_burning_distance - 5 * burning_time

    # Calculate the difference in the final burning distance
    difference = final_burning_distance - initial_burning_distance

    # return the result
    result = difference
    return result

print(solution())