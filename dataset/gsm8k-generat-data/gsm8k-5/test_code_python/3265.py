def solution():
    carla_length_inches = 12  # Carla's brush is 12 inches long
    carmen_length_inches = 1.5 * carla_length_inches  # Carmen's brush is 50% longer than Carla's brush

    # Convert the lengths to centimeters
    carla_length_cm = carla_length_inches * 2.5
    carmen_length_cm = carmen_length_inches * 2.5
    result = carmen_length_cm
    return result

print(solution())