def solution():
    """A roll of 25 m wire weighs 5 kg. How much does a 75 m roll weigh?"""
    # Define the weight per meter of wire
    weight_per_meter = 5 / 25

    # Calculate the weight of the 75 meter roll
    weight_75m = weight_per_meter * 75

    # Return the result
    result = weight_75m
    return result

print(solution())