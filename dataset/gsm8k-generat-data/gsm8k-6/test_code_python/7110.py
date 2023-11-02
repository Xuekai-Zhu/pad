def solution():
    # Find the number of buckets needed to fill the tank
    buckets_needed = 600 / 5  # each bucket is 5 gallons

    # Calculate the ratio of trips made by Jack and Jill
    jack_ratio = 3
    jill_ratio = 2

    # Set up an equation to find the number of trips made by Jill
    # Let x be the number of trips made by Jill
    # Then, the number of trips made by Jack is 3x
    # The total number of buckets carried by both is 2(3x) + x = 7x
    # Setting 7x = buckets_needed, we can solve for x
    x = buckets_needed / 7

    # Round up to the nearest whole number, since Jill cannot make a fraction of a trip
    trips_jill = math.ceil(x)

    result = trips_jill
    return result

print(solution())