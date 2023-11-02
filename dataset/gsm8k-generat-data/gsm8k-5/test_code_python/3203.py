def solution():
    bags = 80  # 80 bags of cement
    weight = 50  # Each bag weighs 50 kgs
    cost = 6000  # Transportation cost for 80 bags is $6000

    # Calculate the cost per kg of cement
    cost_per_kg = cost / (bags * weight)

    # Calculate the new number of bags and weight
    new_bags = bags * 3  # Three times as many bags
    new_weight = weight * (3/5)  # Each bag weighs 3/5 times as much

    # Calculate the new transportation cost
    new_cost = new_bags * new_weight * cost_per_kg
    result = new_cost
    return result

print(solution())