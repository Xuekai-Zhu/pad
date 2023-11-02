def solution():
    """Marta is weighing fruit at the grocery store. The apples weigh four ounces each and the oranges weight 3 ounces. Each plastic bag in the grocery store can hold 49 ounces of fruit before it splits. If Martha wants to put an equal number of apples and oranges in each bag, and she wants to buy 3 full bags of fruit, how many ounces of apples should she buy?"""
    apple_weight = 4
    orange_weight = 3
    bag_capacity = 49
    total_fruit_weight = bag_capacity * 3
    total_apple_weight = (total_fruit_weight / 2) * (apple_weight / (apple_weight + orange_weight))
    result = total_apple_weight
    return result

print(solution())