def solution():
    # Calculate the screen space of each TV
    screen_space_bill = 48 * 100  # 4800 square inches
    screen_space_bob = 70 * 60  # 4200 square inches

    # Calculate the weight of each TV in ounces
    weight_bill = screen_space_bill * 4  # 19200 ounces
    weight_bob = screen_space_bob * 4  # 16800 ounces

    # Calculate the weight difference in pounds
    weight_difference = (weight_bill - weight_bob) / 16  # 750 pounds
    result = weight_difference
    return result

print(solution())