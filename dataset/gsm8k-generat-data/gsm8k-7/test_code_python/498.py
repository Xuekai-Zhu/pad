def solution():
    num_people = 6
    num_bags_per_person = 5
    bag_weight = 50
    max_luggage_weight = 6000

    # Calculate the total weight of all the luggage for the 6 people
    total_luggage_weight = num_people * num_bags_per_person * bag_weight

    # Calculate the amount of weight the plane can still carry
    remaining_weight = max_luggage_weight - total_luggage_weight

    # Calculate the maximum number of bags that can be added at maximum weight
    max_num_bags = remaining_weight // bag_weight
    result = max_num_bags
    return result

print(solution())