def solution():
    weight = 300  # James can do a farmer's walk with 300 pounds per hand for 20 meters
    distance_1 = 20  # James walks 20 meters without straps
    distance_2 = 10  # James walks 10 meters with straps
    increase = 50  # James increases his weight by 50 pounds when he increases his distance without straps
    lift_increase = 0.3  # James can lift 30% more if he only goes 10 meters
    strap_increase = 0.2  # Lifting straps give James another 20%

    # Calculate James' weight for 10 meters without straps
    adjusted_weight = weight * (1 + (increase / (distance_1 * 2)))
    weight_1 = adjusted_weight * (1 + lift_increase)

    # Calculate James' weight for 10 meters with lifting straps
    weight_2 = (weight_1 * (1 + strap_increase))

    result = weight_2
    return result

print(solution())