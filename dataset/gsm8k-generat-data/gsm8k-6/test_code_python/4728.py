def solution():
    # Calculate the total weight of onions harvested by Titan's father
    weight_per_bag = 50  # the weight of each bag of onions
    bags_per_trip = 10   # the number of bags carried per trip
    trips = 20           # the number of trips made by the pickup
    total_bags = bags_per_trip * trips  # the total number of bags transported
    total_weight = total_bags * weight_per_bag  # the total weight of onions harvested
    result = total_weight
    return result

print(solution())