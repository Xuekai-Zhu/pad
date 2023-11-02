def solution():
    bags_per_trip = 10  # James can carry 10 bags on each trip
    trips_per_day = 20  # James takes 20 trips a day
    days = 5  # James works for 5 days

    # Calculate the total number of bags delivered in 5 days
    total_bags = bags_per_trip * trips_per_day * days
    result = total_bags
    return result

print(solution())