def solution():
    # Define the weight of one bottle cap in ounces
    cap_weight = 1/7

    # Convert the total weight of the collection from pounds to ounces
    total_weight_in_ounces = 18 * 16

    # Calculate the number of bottle caps in the collection
    num_caps = total_weight_in_ounces / cap_weight

    result = num_caps
    return result

print(solution())