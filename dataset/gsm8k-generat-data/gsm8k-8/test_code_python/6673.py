def solution():
    # Calculate the total time Sherman spends commuting to and from work each day
    daily_commute_time = 30 + 30

    # Calculate the total time Sherman spends driving his kids each weekend day
    weekend_driving_time = 2 * 60

    # Calculate the total time Sherman spends driving in a week
    total_driving_time = daily_commute_time * 5 + weekend_driving_time * 2

    # Convert the total driving time to hours
    total_driving_hours = total_driving_time / 60

    result = total_driving_hours
    return result

print(solution())