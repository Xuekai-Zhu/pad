def solution():
    num_packs_of_15 = 4
    cupcakes_per_pack_15 = 15
    cupcakes_per_pack_10 = 10
    num_children = 100

    # Calculate the total number of cupcakes Jean has
    total_cupcakes = num_packs_of_15 * cupcakes_per_pack_15

    # Calculate the number of cupcakes Jean needs to give to the children
    cupcakes_needed = num_children

    # Calculate the number of packs of 10 cupcakes Jean needs to buy
    num_packs_of_10_needed = (cupcakes_needed - total_cupcakes) / cupcakes_per_pack_10

    # Round up the number of packs needed since Jean cannot buy partial packs
    num_packs_of_10_needed = math.ceil(num_packs_of_10_needed)

    result = num_packs_of_10_needed
    return result

print(solution())