def solution():
    distance_mon_to_wed = 3 * 3  # Scott runs 3 miles Monday through Wednesday
    distance_thu_fri = 2 * distance_mon_to_wed  # Scott runs twice the distance he ran on Monday on Thursday and Friday
    distance_per_week = distance_mon_to_wed + distance_thu_fri  # Total distance run per week
    weeks_in_month = 4
    total_distance = distance_per_week * weeks_in_month  # Total distance run in a month

    result = total_distance
    return result

print(solution())