def solution():
    """James took a job delivering groceries in his neighborhood. He can carry 10 bags on each trip. If he takes 20 trips a day, how many bags does he deliver in 5 days?"""
    bags_per_trip = 10
    trips_per_day = 20
    num_days = 5
    bags_delivered = bags_per_trip * trips_per_day * num_days
    result = bags_delivered
    return result

print(solution())