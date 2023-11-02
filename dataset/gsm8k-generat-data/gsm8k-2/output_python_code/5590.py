def solution():
    """Chris wants to hold his breath underwater for 90 straight seconds so he starts training each day. On the first day, he holds it for 10 seconds. On the second day, he holds it for 20 seconds. On the third day, he holds it for 30 seconds. After realizing that he can hold it for ten extra seconds each day, he realizes he can calculate how many days it is until he reaches 90 if he keeps up the same pace. So how many days until he can hold his breath for 90 seconds?"""
    current_time = 30
    extra_time_per_day = 10
    days = 3
    while current_time < 90:
        current_time += extra_time_per_day
        days += 1
    result = days
    return result

print(solution())