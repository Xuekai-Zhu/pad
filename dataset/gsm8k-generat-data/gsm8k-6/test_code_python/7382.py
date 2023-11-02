def solution():
    # Calculate the number of steaks Tommy needs to buy
    total_pounds = 5  # each member wants 1 pound of steak
    steak_weight_ounces = 20  # each steak weighs 20 ounces
    steaks_needed = total_pounds * 16 / steak_weight_ounces  # convert pounds to ounces
    result = steaks_needed
    return result

print(solution())