def solution():
    """Carla's brush is 12 inches long. If Carmen's brush is 50% longer than Carla's brush, how long is Carmen's brush in centimeters? (There are 2.5 centimeters per inch.)"""
    # Define the length of Carla's brush in inches
    carla_length = 12

    # Calculate the length of Carmen's brush in inches
    carmen_length = carla_length * 1.5

    # Convert the length of Carmen's brush to centimeters
    carmen_length_cm = carmen_length * 2.5

    # Display the length of Carmen's brush in centimeters
    result = carmen_length_cm
    return result

print(solution())