def solution():
    total_beef_pounds = 15
    steak_weight_ounces = 12

    # Convert pounds to ounces
    total_beef_ounces = total_beef_pounds * 16

    # Calculate the total number of steaks
    num_steaks = total_beef_ounces // steak_weight_ounces

    result = num_steaks
    return result

print(solution())