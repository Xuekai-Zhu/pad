def solution():
    # Calculate the total distance Jerry runs roundtrip
    jerry_distance = 2 * 4  # Jerry runs from his house to school and back

    # Calculate the time it takes Jerry to make a roundtrip
    jerry_time = 2 * 15/60  # Jerry takes 15 minutes for one-way trip, so roundtrip takes twice as long

    # Calculate Carson's speed
    carson_speed = jerry_distance / jerry_time
    result = carson_speed
    return result

print(solution())