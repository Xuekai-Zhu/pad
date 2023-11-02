def solution():
    """James took a job delivering groceries in his neighborhood. He can carry 10 bags on each trip. If he takes 20 trips a day, how many bags does he deliver in 5 days?"""
    # Define the number of bags per trip and the number of trips per day
    bags_per_trip = 10
    trips_per_day = 20

    # Calculate the number of bags delivered in one day
    bags_per_day = bags_per_trip * trips_per_day

    # Calculate the number of bags delivered in five days
    bags_in_5_days = bags_per_day * 5

    result = bags_in_5_days
    return result

print(solution())