def solution():
    """Jackie walks 2 miles each day while Jessie walks 1.5 miles each day. How many more miles, in all, does Jackie walk than Jessie walk in 6 days?"""
    jackie_miles_per_day = 2
    jessie_miles_per_day = 1.5
    total_days = 6
    jackie_total_miles = jackie_miles_per_day * total_days
    jessie_total_miles = jessie_miles_per_day * total_days
    difference = jackie_total_miles - jessie_total_miles
    result = difference
    return result

print(solution())