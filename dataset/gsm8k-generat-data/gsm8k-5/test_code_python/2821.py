def solution():
    beef_weight = 15  # Matt orders 15 pounds of beef
    steak_weight = 12  # Each steak weighs 12 ounces

    # Convert beef weight to ounces
    beef_weight_ounces = beef_weight * 16

    # Calculate the number of steaks Matt can get
    num_steaks = beef_weight_ounces / steak_weight
    result = num_steaks
    return result

print(solution())