def solution():
    """A shop sold 29 bags of potatoes in the morning. In the afternoon, the shop sold 17 bags of potatoes. If each bag of potatoes weighs 7kg, how many kilograms of potatoes did the shop sell for the whole day?"""
    # Define the number of bags sold in the morning and afternoon
    morning_bags = 29
    afternoon_bags = 17

    # Calculate the total number of bags sold
    total_bags = morning_bags + afternoon_bags

    # Calculate the total weight of the potatoes sold
    total_weight = total_bags * 7

    # return the result
    result = total_weight
    return result

print(solution())