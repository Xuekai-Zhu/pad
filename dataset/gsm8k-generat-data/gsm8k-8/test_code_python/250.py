def solution():
    # Calculate the total weight of the plates without the special technology
    total_weight = 10 * 30

    # Calculate the weight increase due to the special technology
    increase = total_weight * 0.2

    # Calculate the total weight with the special technology
    total_weight_with_tech = total_weight + increase

    # Calculate the weight per plate with the special technology
    weight_per_plate_with_tech = total_weight_with_tech / 10
    result = weight_per_plate_with_tech
    return result

print(solution())