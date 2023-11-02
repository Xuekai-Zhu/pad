def solution():
    """Dabbie bought 3 turkeys for thanksgiving, the first turkey is 6 kilograms, the second turkey is 9 kilograms, and the weight of the third turkey is twice the weight of the second turkey. 
    If the cost of a kilogram of turkey is $2, how much does Dabbie spent on all the turkeys?"""
    turkey1_weight = 6
    turkey2_weight = 9
    turkey3_weight = 2 * turkey2_weight
    price_per_kilogram = 2
    total_cost = (turkey1_weight + turkey2_weight + turkey3_weight) * price_per_kilogram
    result = total_cost
    return result

print(solution())