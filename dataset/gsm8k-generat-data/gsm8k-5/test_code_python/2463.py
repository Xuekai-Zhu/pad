def solution():
    initial_count = 300  # Initial count of athletes
    departure_rate = 28  # Rate at which athletes left the camp in the morning
    arrival_rate = 15  # Rate at which athletes arrived at the camp later in the day

    # Calculate the number of athletes that left the camp in the morning
    morning_departure = departure_rate * 4

    # Calculate the number of athletes that arrived at the camp later in the day
    late_arrivals = arrival_rate * 7

    # Calculate the final count of athletes
    final_count = initial_count - morning_departure + late_arrivals

    # Calculate the difference in the total number of athletes over the two nights
    difference = final_count - initial_count
    result = difference
    return result

print(solution())