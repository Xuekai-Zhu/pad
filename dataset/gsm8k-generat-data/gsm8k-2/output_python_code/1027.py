def solution():
    """A bar of steel weighs twice the mass of a bar of tin. If a steel bar also weighs 20 kgs more than a copper bar and a copper bar weighs 90 kgs, calculate the total weight of a container with 20 bars of each type of metal."""
    copper_weight = 90
    steel_weight = copper_weight + 20
    tin_weight = steel_weight / 2
    total_weight = (copper_weight + steel_weight + tin_weight) * 20
    result = total_weight
    return result

print(solution())