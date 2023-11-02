def solution():
    # Define the hike distance and pack weight ratio
    hike_distance = 2.5 * 8 * 5
    pack_ratio = 0.5

    # Calculate the weight of supplies needed for the entire hike
    total_weight = hike_distance * pack_ratio

    # Calculate the weight of supplies needed for the first half of the hike
    first_half_weight = total_weight / 2

    # Calculate the weight of supplies needed for the second half of the hike
    second_half_weight = first_half_weight * 0.25

    # Calculate the total weight of supplies needed for the entire hike, accounting for the resupply
    final_weight = first_half_weight + second_half_weight

    result = final_weight
    return result

print(solution())