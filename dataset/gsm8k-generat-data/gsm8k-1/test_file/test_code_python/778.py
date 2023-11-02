def solution():
    """Chase and Rider can ride their bikes thrice a day for 5 days; but on two other days, they ride twice the times they do on usual days. How many times do they ride their bikes a week?"""
    usual_rides_per_day = 3
    usual_days = 5
    usual_weekly_rides = usual_rides_per_day * usual_days

    extra_rides_per_day = usual_rides_per_day * 2
    extra_days = 2
    extra_weekly_rides = extra_rides_per_day * extra_days

    total_weekly_rides = usual_weekly_rides + extra_weekly_rides
    result = total_weekly_rides

    return result

print(solution())