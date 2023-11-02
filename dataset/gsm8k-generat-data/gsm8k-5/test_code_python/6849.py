def solution():
    distance = 143  # Mobius is traveling 143 miles from Florence to Rome and back
    usual_speed = 13  # Mobius' usual top speed without any load is 13 miles per hour
    loaded_speed = 11  # Mobius' top speed with a typical load is 11 miles per hour
    rest_time = 1  # Mobius takes two 30-minute rest stops during each half of the trip
    half_distance = distance / 2

    # Calculate the time taken to travel from Florence to Rome with a load and two rest stops
    time_to_rome = half_distance / loaded_speed + rest_time

    # Calculate the time taken to travel from Rome to Florence without a load and two rest stops
    time_to_home = half_distance / usual_speed + rest_time

    # Calculate the total time taken for the round trip
    total_time = time_to_rome + time_to_home
    result = total_time
    return result

print(solution())