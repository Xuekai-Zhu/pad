def solution():
    meters_per_mile = 1609
    race_distance = 26 * meters_per_mile
    initial_pace = 10 * meters_per_mile / 1
    final_pace = initial_pace * 0.8
    total_time = race_distance / final_pace
 
    return total_time

print(solution())