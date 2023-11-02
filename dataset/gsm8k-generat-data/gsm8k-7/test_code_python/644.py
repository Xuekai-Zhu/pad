def solution():
    daily_passengers = 1200000
    num_weeks = 13

    # Calculate the total number of passengers carried in 13 weeks
    total_passengers = daily_passengers * 7 * num_weeks

    result = total_passengers
    return result

print(solution())