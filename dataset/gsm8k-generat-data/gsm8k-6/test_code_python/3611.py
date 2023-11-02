def solution():
    # Calculate the weight of the third turkey
    weight_third_turkey = 2 * 9  # the weight of the third turkey is twice the weight of the second turkey

    # Calculate the total weight of all the turkeys
    total_weight = 6 + 9 + weight_third_turkey

    # Calculate the total cost of all the turkeys
    total_cost = total_weight * 2  # the cost of a kilogram of turkey is $2

    result = total_cost
    return result

print(solution())