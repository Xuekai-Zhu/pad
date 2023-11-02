def solution():
    
    frosting_for_layer_cake = 1
    frosting_for_single_cake_or_brownie_or_cupcake = 0.5
    total_frosting_needed = frosting_for_layer_cake * 3 + \
        frosting_for_single_cake_or_brownie_or_cupcake * \
        (6 + 12 + 18)
    result = total_frosting_needed
    return result

print(solution())