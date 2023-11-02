def solution():
    round_trip_to_house = 20
    extra_distance_to_supermarket = 10
    days_driving_to_supermarket = 2
    total_driving_days_per_week = 5   # assuming Laura only drives on weekdays

    # Calculate the total distance Laura drives to school per week
    driving_to_school_per_week = round_trip_to_house * total_driving_days_per_week

    # Calculate the total distance Laura drives to the supermarket per week
    driving_to_supermarket_per_week = extra_distance_to_supermarket * days_driving_to_supermarket

    # Calculate the total distance Laura drives per week
    total_driving_distance_per_week = driving_to_school_per_week + driving_to_supermarket_per_week
    result = total_driving_distance_per_week
    return result

print(solution())