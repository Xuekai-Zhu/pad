def solution():
    leakage_rate = 1.5  # ounces per hour
    time_in_hours = 12

    # Calculate the total amount of fluid that will leak over 12 hours
    total_leakage = leakage_rate * time_in_hours

    # Calculate the size of the bucket needed to hold twice the amount of fluid that will leak over 12 hours
    bucket_size = 2 * total_leakage
    result = bucket_size
    return result

print(solution())