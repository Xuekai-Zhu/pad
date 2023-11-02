def solution():
    # Calculate the weight per meter
    weight_per_meter = 5 / 25  # 5 kg for 25 m of wire

    # Calculate the weight of a 75 m roll
    weight_75m = weight_per_meter * 75

    result = weight_75m
    return result

print(solution())