def solution():
    """Titan's father has an onion farm ready for harvest. He borrows Mr. Clay's pickup and transports the harvest to their store, carrying ten bags per trip, prepared for sale. If the onions are in 50 kgs bags, and the pickup makes 20 trips, what's the total weight of onions harvested by Titan's father?"""
    bags_per_trip = 10
    bag_weight = 50
    trips = 20
    total_weight = bags_per_trip * bag_weight * trips
    result = total_weight
    return result

print(solution())