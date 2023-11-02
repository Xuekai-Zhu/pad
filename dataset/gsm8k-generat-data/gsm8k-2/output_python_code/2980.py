def solution():
    """Jackie walks 2 miles each day while Jessie walks 1.5 miles each day. How many more miles, in all, does Jackie walk than Jessie walk in 6 days?"""
    jackie_daily_distance = 2
    jessie_daily_distance = 1.5
    num_days = 6
    jackie_total_distance = jackie_daily_distance * num_days
    jessie_total_distance = jessie_daily_distance * num_days
    difference = jackie_total_distance - jessie_total_distance
    result = difference
    return result

print(solution())