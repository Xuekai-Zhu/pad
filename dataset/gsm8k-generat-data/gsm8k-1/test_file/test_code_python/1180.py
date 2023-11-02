def solution():
    """To heat during the winter, Ali ordered 850kg of coal. The coal is delivered in 50kg bags, costing $18 per unit. How much does his order cost?"""
    coal_weight = 850
    bag_weight = 50
    bags_required = coal_weight / bag_weight
    bag_cost = 18
    total_cost = bags_required * bag_cost
    result = total_cost
    return result

print(solution())