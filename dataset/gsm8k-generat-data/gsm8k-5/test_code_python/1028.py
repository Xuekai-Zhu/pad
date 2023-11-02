def solution():
    # Calculate the weight of the steel bar
    copper_weight = 90  # given
    steel_weight = copper_weight + 20  # Steel bar weighs 20 kgs more than copper bar
    tin_weight = steel_weight / 2  # Steel bar weighs twice the mass of tin bar

    # Calculate the total weight of each type of metal
    total_copper_weight = 20 * copper_weight
    total_tin_weight = 20 * tin_weight
    total_steel_weight = 20 * steel_weight

    # Calculate the total weight of the container
    total_weight = total_copper_weight + total_tin_weight + total_steel_weight
    result = total_weight
    return result

print(solution())