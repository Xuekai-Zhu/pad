def solution():
    
    store_trips_per_month = 4
    dollars_spent_per_trip = 2
    months_in_a_year = 12
    dollars_left_after_year = 104
    total_dollars_spent = store_trips_per_month * dollars_spent_per_trip * months_in_a_year
    initial_dollars = total_dollars_spent + dollars_left_after_year
    result = initial_dollars
    return result

print(solution())