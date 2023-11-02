def solution():
    breakfast_time = 20
    lunch_time = 5
    dinner_time_4_days = 10
    dinner_time_rest_of_days = 30
    num_days_4_dinner_10 = 4

    # Calculate the total time Polly spends cooking dinner for 4 days
    total_dinner_time_4_days = dinner_time_4_days * num_days_4_dinner_10

    # Calculate the total time Polly spends cooking dinner for the rest of the days
    total_dinner_time_rest_of_days = dinner_time_rest_of_days * (7 - num_days_4_dinner_10)

    # Calculate the total time Polly spends cooking for the week
    total_time = breakfast_time + lunch_time + total_dinner_time_4_days + total_dinner_time_rest_of_days
    result = total_time
    return result

print(solution())