def solution():
    """Jake trips over his dog 40% percent of mornings. 25% of the time he trips, he drops his coffee. What percentage of mornings does he NOT drop his coffee?"""
    trip_freq = 0.4
    drop_freq_given_trip = 0.25
    no_drop_freq_given_trip = 1 - drop_freq_given_trip
    no_drop_freq_given_no_trip = 1
    no_trip_freq = 1 - trip_freq
    
    # probability of no drop
    no_drop_freq = (no_trip_freq * no_drop_freq_given_no_trip) + (trip_freq * no_drop_freq_given_trip)
    
    result = no_drop_freq * 100  # result in percentage
    
    return result

print(solution())