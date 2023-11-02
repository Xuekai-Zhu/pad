def solution():
    num_days = 5
    avg_daily_hours = 2

    mon_to_wed_avg_speed = 12
    thu_to_fri_avg_speed = 9

    # Calculate the total distance traveled from Monday to Wednesday
    mon_to_wed_distance = mon_to_wed_avg_speed * (avg_daily_hours * 3)

    # Calculate the total distance traveled from Thursday to Friday
    thu_to_fri_distance = thu_to_fri_avg_speed * (avg_daily_hours * 2)

    # Calculate the total distance traveled during the 5 days
    total_distance = mon_to_wed_distance + thu_to_fri_distance
    result = total_distance
    return result

print(solution())