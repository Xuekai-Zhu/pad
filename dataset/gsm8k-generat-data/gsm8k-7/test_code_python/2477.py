def solution():
    total_wages = 160
    hours_per_week = 12
    wage_per_hour = 9

    # Calculate the total wages for the second job
    total_wages_second_job = hours_per_week * wage_per_hour

    # Calculate the wages for the first job by subtracting the wages from the second job
    wages_first_job = total_wages - total_wages_second_job
    result = wages_first_job
    return result

print(solution())