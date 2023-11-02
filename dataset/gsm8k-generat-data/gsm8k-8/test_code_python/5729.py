def solution():
    # Calculate the number of feathers Milly needs in total
    num_feathers = 12 * 200

    # Calculate the number of flamingos needed to harvest
    num_flamingos = num_feathers / (20 * 0.25)

    # Round up to the nearest whole number
    num_flamingos = int(num_flamingos + 0.5)

    result = num_flamingos
    return result

print(solution())