def solution():
    # Calculate the total distance Jerry covers in a round trip
    jerry_distance = 2 * 4  # Jerry runs from his house to school and back, the school is 4 miles away

    # Calculate the time Jerry takes for a round trip
    jerry_time = 2 * 15  # Jerry takes 15 minutes for one-way trip, so round trip takes 30 mins = 0.5 hours

    # Calculate the speed of Carson
    carson_speed = jerry_distance / jerry_time  # Carson takes the same time as Jerry for half the distance
    carson_speed_mph = carson_speed * 60  # converting speed from miles per minute to miles per hour

    result = carson_speed_mph
    return result

print(solution())