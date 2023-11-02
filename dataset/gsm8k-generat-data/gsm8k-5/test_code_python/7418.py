def solution():
    ounces_per_pound = 16  # There are 16 ounces in a pound
    bottle_caps_per_ounce = 7  # 7 bottle caps weigh one ounce
    total_weight_ounces = 18 * ounces_per_pound  # Convert total weight to ounces
    total_bottle_caps = total_weight_ounces * bottle_caps_per_ounce  # Calculate total bottle caps

    result = total_bottle_caps
    return result

print(solution())