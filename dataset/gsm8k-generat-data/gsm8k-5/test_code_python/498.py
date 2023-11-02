def solution():
    num_people = 6  # There are 6 people going on the trip
    num_bags_each = 5  # Each person has 5 bags of luggage
    weight_each_bag = 50  # Each bag weighs 50 pounds
    max_weight_plane = 6000  # The airplane can hold a total luggage weight of 6000 pounds

    # Calculate the total weight of the luggage of all 6 people
    total_weight_luggage = num_people * num_bags_each * weight_each_bag

    # Calculate the maximum number of bags the plane can hold at maximum weight
    max_num_bags = (max_weight_plane - total_weight_luggage) / weight_each_bag
    result = max_num_bags
    return result

print(solution())