def solution():
    """A roll of 25 m wire weighs 5 kg. How much does a 75 m roll weigh?"""
    # Calculate the weight per meter of wire
    weight_per_meter = 5 / 25  # 5 kg / 25 m = 0.2 kg/m

    # Calculate the weight of a 75 m roll
    roll_weight = weight_per_meter * 75

    # Display the weight of the 75 m roll
    result = roll_weight
    return result

print(solution())