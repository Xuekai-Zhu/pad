def solution():
    """Marta is weighing fruit at the grocery store. The apples weigh four ounces each and the oranges weight 3 ounces. Each plastic bag in the grocery store can hold 49 ounces of fruit before it splits. If Martha wants to put an equal number of apples and oranges in each bag, and she wants to buy 3 full bags of fruit, how many ounces of apples should she buy?"""
    bag_capacity = 49
    apples_weight = 4
    oranges_weight = 3
    fruit_per_bag = bag_capacity / (apples_weight + oranges_weight)
    # since Martha wants equal number of apples and oranges in each bag, we use floor division to get the number of apples that can fit in each bag
    apples_per_bag = fruit_per_bag // 2
    total_apples = apples_per_bag * 3
    total_weight = total_apples * apples_weight
    result = total_weight
    return result

print(solution())