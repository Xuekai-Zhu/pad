def solution():
    """A shop sold 29 bags of potatoes in the morning. In the afternoon, the shop sold 17 bags of potatoes. If each bag of potatoes weighs 7kg, how many kilograms of potatoes did the shop sell for the whole day?"""
    morning_bags = 29
    afternoon_bags = 17
    bag_weight = 7
    total_kg = (morning_bags + afternoon_bags) * bag_weight
    result = total_kg
    return result

print(solution())