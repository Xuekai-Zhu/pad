def solution():
    """There are 6 people going on an airplane trip. They each have 5 bags of luggage. Each of their bags weighs the maximum weight allowed, 50 pounds. The airplane can hold a total luggage weight of 6000 pounds. How many more bags at maximum weight can the plane hold?"""
    # Define the number of people and bags of luggage per person
    people = 6
    bags_per_person = 5

    # Define the maximum weight per bag
    max_weight_per_bag = 50

    # Calculate the total weight of the luggage brought by the people
    total_weight = people * bags_per_person * max_weight_per_bag

    # Calculate the maximum weight the plane can hold
    max_weight_plane = 6000

    # Calculate the remaining weight the plane can hold
    remaining_weight = max_weight_plane - total_weight

    # Calculate the number of bags at maximum weight that can be added to the plane
    remaining_bags = remaining_weight // max_weight_per_bag

    result = remaining_bags
    return result

print(solution())