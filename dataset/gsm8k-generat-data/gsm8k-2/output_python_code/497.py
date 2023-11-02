def solution():
    """There are 6 people going on an airplane trip. They each have 5 bags of luggage. Each of their bags weighs the maximum weight allowed, 50 pounds. The airplane can hold a total luggage weight of 6000 pounds. How many more bags at maximum weight can the plane hold?"""
    num_people = 6
    num_bags_per_person = 5
    bag_weight = 50
    total_luggage_weight = num_people * num_bags_per_person * bag_weight
    remaining_weight_capacity = 6000 - total_luggage_weight
    remaining_bags_capacity = remaining_weight_capacity / bag_weight
    result = remaining_bags_capacity
    return result

print(solution())