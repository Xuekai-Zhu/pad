def solution():
    jackie_daily_distance = 2
    jessie_daily_distance = 1.5
    num_days = 6

    # Calculate the total distance Jackie walks in 6 days
    total_jackie_distance = jackie_daily_distance * num_days

    # Calculate the total distance Jessie walks in 6 days
    total_jessie_distance = jessie_daily_distance * num_days

    # Calculate the difference between the total distance Jackie walks and the total distance Jessie walks
    difference_distance = total_jackie_distance - total_jessie_distance
    result = difference_distance
    return result

print(solution())