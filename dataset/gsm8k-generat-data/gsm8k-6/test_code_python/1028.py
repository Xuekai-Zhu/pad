def solution():
    # Calculate the weight of the steel, tin, and copper bars
    copper_weight = 90  # given
    steel_weight = copper_weight + 20  # steel bar weighs 20 kgs more than copper bar
    tin_weight = steel_weight / 2  # steel bar weighs twice the mass of tin bar

    # Calculate the total weight of 20 bars of each type
    total_weight = (copper_weight * 20) + (steel_weight * 20) + (tin_weight * 20)
    result = total_weight
    return result

print(solution())