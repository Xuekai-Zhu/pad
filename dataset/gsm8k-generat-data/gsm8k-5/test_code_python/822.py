def solution():
    cupcakes_per_pack1 = 10  # Cupcakes are sold in packages of 10
    cupcakes_per_pack2 = 15  # Cupcakes are sold in packages of 15
    packs_bought = 4  # Jean bought 4 packs of 15 cupcakes
    cupcakes_given = 100  # Jean wants to give one cupcake each to 100 children

    # Calculate the total number of cupcakes bought
    total_cupcakes = packs_bought * cupcakes_per_pack2

    # Calculate the number of cupcakes remaining after giving one to each child
    remaining_cupcakes = total_cupcakes - cupcakes_given

    # Calculate the number of packs of 10 cupcakes needed to buy
    packs_required = remaining_cupcakes / cupcakes_per_pack1
    result = packs_required
    return result

print(solution())