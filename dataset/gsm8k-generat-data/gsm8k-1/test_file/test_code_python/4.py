def solution():
    """John drives for 3 hours at a speed of 60 mph and then turns around because he realizes he forgot something very important at home. He tries to get home in 4 hours but spends the first 2 hours in standstill traffic. He spends the next half-hour driving at a speed of 30mph, before being able to drive the remaining time of the 4 hours going at 80 mph. How far is he from home at the end of those 4 hours?"""
    distance_from_home = 3 * 60  # 180 miles
    time_spent_in_traffic = 2
    time_spent_driving_slowly = 0.5
    time_spent_driving_fast = 4 - time_spent_in_traffic - time_spent_driving_slowly
    distance_driven_slowly = 30 * time_spent_driving_slowly  # 15 miles
    distance_driven_fast = 80 * time_spent_driving_fast  # 240 miles
    total_distance_from_home = distance_from_home + distance_driven_slowly - distance_driven_fast
    result = total_distance_from_home
    return result

print(solution())