def solution():
    driving_time_per_day = 40/60  # Jessica drives to and from school every day, which is 20 minutes each way
    total_driving_hours = 50  # Jessica needs to complete 50 hours of driving with a parent
    driving_days = total_driving_hours / driving_time_per_day  # Calculate the total number of driving days needed
    result = driving_days
    return result

print(solution())