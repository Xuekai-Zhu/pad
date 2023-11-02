def solution():
    # Calculate the total biking distance in a week
    daily_distance = 20 * 2  # Tim rides back and forth to work, so daily distance is 20 miles
    weekly_distance = (daily_distance * 5) + 200  # Tim bikes to work for 5 days and goes on a weekend ride
    biking_time = weekly_distance / 25  # Tim can bike at 25 mph, so the time he spends biking is the distance divided by speed
    result = biking_time
    return result

print(solution())