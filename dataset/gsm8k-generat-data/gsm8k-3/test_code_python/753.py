def solution():
    """A shop sold 29 bags of potatoes in the morning. In the afternoon, the shop sold 17 bags of potatoes. If each bag of potatoes weighs 7kg, how many kilograms of potatoes did the shop sell for the whole day?"""
    # Define the number of bags of potatoes sold in the morning and afternoon
    MORNING_BAGS = 29
    AFTERNOON_BAGS = 17

    # Define the weight of each bag of potatoes
    BAG_WEIGHT = 7

    # Calculate the total weight of potatoes sold
    total_weight = (MORNING_BAGS + AFTERNOON_BAGS) * BAG_WEIGHT

    # Display the total weight of potatoes sold
    result = total_weight
    return result

print(solution())