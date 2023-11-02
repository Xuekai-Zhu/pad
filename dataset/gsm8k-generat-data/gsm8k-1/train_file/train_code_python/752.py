def solution():
    """A shop sold 29 bags of potatoes in the morning. In the afternoon, the shop sold 17 bags of potatoes. If each bag of potatoes weighs 7kg, how many kilograms of potatoes did the shop sell for the whole day?"""
    bags_morning = 29
    bags_afternoon = 17
    bags_total = bags_morning + bags_afternoon
    weight_per_bag = 7
    total_weight = bags_total * weight_per_bag
    result = total_weight
    return result

print(solution())