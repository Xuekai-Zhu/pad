def solution():
    """Tim rides his bike back and forth to work for each of his 5 workdays. His work is 20 miles away. He also goes for a weekend bike ride of 200 miles. If he can bike at 25 mph how much time does he spend biking a week?"""
    # Define the distance to work and the weekend ride
    work_distance = 20 * 2 # round-trip distance
    weekend_ride_distance = 200

    # Calculate the total biking distance for the week
    total_distance = work_distance * 5 + weekend_ride_distance

    # Calculate the time spent biking
    time_spent_biking = total_distance / 25

    # return the result
    result = time_spent_biking
    return result

print(solution())