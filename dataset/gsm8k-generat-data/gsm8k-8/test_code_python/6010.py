def solution():
    # Define initial values
    weight = 300
    distance_1 = 20
    distance_2 = 10
    increase = 50
    lift_increase = 0.3
    strap_increase = 0.2

    # Calculate new weight for 20 meters and apply increase
    new_weight = weight + increase
    new_weight_lift = new_weight * (1 + lift_increase)

    # Calculate weight with lifting straps for 10 meters and apply increase
    weight_with_straps = new_weight_lift * (1 + strap_increase)
    weight_with_straps_lift = weight_with_straps * (1 + lift_increase)

    # Calculate the total weight for 10 meters
    total_weight = weight_with_straps_lift * (distance_2 / distance_1)

    result = total_weight
    return result

print(solution())