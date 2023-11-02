def solution():
    num_days = 3
    jade_hours_per_day = 8
    krista_hours_per_day = 6

    # Calculate the total number of hours Jade drove
    jade_total_hours = jade_hours_per_day * num_days

    # Calculate the total number of hours Krista drove
    krista_total_hours = krista_hours_per_day * num_days

    # Calculate the total number of hours they drove altogether
    total_hours = jade_total_hours + krista_total_hours
    result = total_hours
    return result

print(solution())