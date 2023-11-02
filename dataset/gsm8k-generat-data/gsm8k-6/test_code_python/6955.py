def solution():
    # Find the total practice time from Tuesday to Thursday
    practice_time_Tuesday = x
    practice_time_Wednesday = x + 5
    practice_time_Thursday = 50
    total_practice_time = practice_time_Tuesday + practice_time_Wednesday + practice_time_Thursday

    # Find the required practice time for Monday
    practice_time_Monday = 2 * practice_time_Tuesday

    # Find the required practice time for Friday
    total_week_practice_time = 5 * 60  # 5 hours in minutes
    practice_time_Friday = total_week_practice_time - practice_time_Monday - total_practice_time

    result = practice_time_Friday
    return result

print(solution())