def solution():
    bags_per_trip = 10  # The pickup carries 10 bags per trip
    bag_weight = 50  # The bags are 50 kgs each
    trips = 20  # The pickup makes 20 trips to transport the harvest

    # Calculate the total weight of onions harvested
    total_weight = bags_per_trip * bag_weight * trips
    result = total_weight
    return result

print(solution())