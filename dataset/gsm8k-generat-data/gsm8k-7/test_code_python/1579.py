def solution():
    hours_charged = 10
    usage_per_hour = 2
    fraction_charged = 3/5

    # Calculate the total time the phone would last if charged for the fraction of time
    # Olive charged it last night
    total_usage_time = fraction_charged * hours_charged * usage_per_hour
    result = total_usage_time
    return result

print(solution())