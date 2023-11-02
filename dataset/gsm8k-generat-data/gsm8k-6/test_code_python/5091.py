def solution():
    # Calculate the total cans of frosting needed for all the baked goods
    frosting_for_single_cake = 0.5
    frosting_for_single_brownie = 0.5
    frosting_for_dozen_cupcakes = 0.5 * 12
    frosting_for_three_layer_cakes = 3
    frosting_for_all_goods = (frosting_for_single_cake * 12) + (frosting_for_single_brownie * 18) + frosting_for_dozen_cupcakes + frosting_for_three_layer_cakes

    result = frosting_for_all_goods
    return result

print(solution())