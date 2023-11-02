def solution():
    length1 = 25
    weight1 = 5
    length2 = 75

    # Calculate the weight per meter of wire
    weight_per_meter = weight1 / length1

    # Calculate the weight of the 75 m roll
    weight2 = weight_per_meter * length2
    result = weight2
    return result

print(solution())