def solution():
    # Define the weight of one shirt and one pair of pants
    shirt_weight = 1/4
    pants_weight = 1/2

    # Calculate the total weight of the shirts and pants
    total_weight = 20 * shirt_weight + 20 * pants_weight

    # Calculate the number of loads needed, rounding up to the nearest integer
    loads_needed = math.ceil(total_weight / 5)

    result = loads_needed
    return result

print(solution())