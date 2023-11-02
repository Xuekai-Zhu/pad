def solution():
    bags_per_trip = 10
    num_trips_per_day = 20
    num_days = 5

    # Calculate the total number of bags delivered in one day
    bags_per_day = bags_per_trip * num_trips_per_day

    # Calculate the total number of bags delivered in five days
    total_bags_delivered = bags_per_day * num_days
    result = total_bags_delivered
    return result

print(solution())