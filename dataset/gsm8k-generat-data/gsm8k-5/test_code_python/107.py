def solution():
    tuesday_traffic = 25
    monday_traffic = 0.8 * tuesday_traffic  # 20% less than Tuesday
    wednesday_traffic = monday_traffic + 2  # 2 more cars than Monday
    weekday_traffic = tuesday_traffic + monday_traffic + wednesday_traffic + 10 + 10  # Thursday and Friday have 10 cars each
    weekend_traffic = 5 * 2  # Saturday and Sunday each have 5 cars
    total_traffic = weekday_traffic + weekend_traffic
    result = total_traffic
    return result

print(solution())