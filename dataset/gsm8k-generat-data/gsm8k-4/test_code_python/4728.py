def solution():
    """Titan's father has an onion farm ready for harvest. He borrows Mr. Clay's pickup and transports the harvest to their store, carrying ten bags per trip, prepared for sale. If the onions are in 50 kgs bags, and the pickup makes 20 trips, what's the total weight of onions harvested by Titan's father?"""
    # Define the number of bags per trip and the weight per bag
    BAGS_PER_TRIP = 10
    BAG_WEIGHT = 50

    # Calculate the total weight of onions harvested
    total_weight = BAGS_PER_TRIP * BAG_WEIGHT * 20

    # return the result
    result = total_weight
    return result

print(solution())