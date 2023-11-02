def solution():
    """Dabbie bought 3 turkeys for thanksgiving, the first turkey is 6 kilograms, the second turkey is 9 kilograms, and the weight of the third turkey is twice the weight of the second turkey. If the cost of a kilogram of turkey is $2, how much does Dabbie spent on all the turkeys?"""
    # Define the cost per kilogram of turkey
    cost_per_kilo = 2

    # Calculate the weight of the third turkey
    third_turkey_weight = 2 * 9

    # Calculate the total weight of the three turkeys
    total_weight = 6 + 9 + third_turkey_weight

    # Calculate the total cost of the turkeys
    total_cost = total_weight * cost_per_kilo

    result = total_cost
    return result

print(solution())