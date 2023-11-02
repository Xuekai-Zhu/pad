def solution():
    """There are 6 people going on an airplane trip.  They each have 5 bags of luggage.  Each of their bags weighs the maximum weight allowed, 50 pounds.  The airplane can hold a total luggage weight of 6000 pounds.  How many more bags at maximum weight can the plane hold?"""
    # Define the number of people and bags per person
    people = 6
    bags_per_person = 5

    # Define the weight per bag
    bag_weight = 50

    # Calculate the total weight of the bags brought by the passengers
    total_weight_passengers = people * bags_per_person * bag_weight

    # Calculate the maximum weight the plane can hold
    max_weight_plane = 6000

    # Calculate the remaining weight the plane can hold
    remaining_weight = max_weight_plane - total_weight_passengers

    # Calculate the maximum number of bags at maximum weight the plane can hold
    max_bags = remaining_weight // bag_weight

    # Display the maximum number of bags the plane can hold at maximum weight
    result = max_bags
    return result

print(solution())