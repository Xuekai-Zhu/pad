def solution():
    # Define the weight and length of the first roll
    weight_roll1 = 5
    length_roll1 = 25

    # Calculate the weight per meter
    weight_per_meter = weight_roll1 / length_roll1

    # Calculate the weight of the second roll
    length_roll2 = 75
    weight_roll2 = weight_per_meter * length_roll2
    result = weight_roll2
    return result

print(solution())