def solution():
    # Calculate the time it takes Mobius to travel from Florence to Rome
    time_florence_to_rome = 143/11

    # Calculate the time it takes Mobius to travel from Rome to Florence
    time_rome_to_florence = 143/13

    # Calculate the total time for the round trip, including rest stops
    total_time = time_florence_to_rome + time_rome_to_florence + 1

    # Convert the two 30-minute rest stops into hours
    rest_stops = 2 * 0.5/60

    # Add the rest stop time to the total time
    total_time_with_rest_stops = total_time + rest_stops

    result = total_time_with_rest_stops
    return result

print(solution())