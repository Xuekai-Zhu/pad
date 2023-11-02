def solution():
    distance_day_1 = 200  # On the first day, they traveled 200 miles
    distance_day_2 = (3/4) * distance_day_1  # On the second day, they traveled 3/4 as far
    distance_day_3 = (1/2) * (distance_day_1 + distance_day_2)  # On the third day, they traveled 1/2 as many miles as the first two days combined

    # Calculate the total distance traveled in 3 days
    total_distance = distance_day_1 + distance_day_2 + distance_day_3
    result = total_distance
    return result

print(solution())