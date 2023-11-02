def solution():
    """Josh found out that 7 bottle caps weigh exactly one ounce. Josh's entire bottle cap collection weighs 18 pounds exactly. How many bottle caps does Josh have in his collection?"""
    # Define the weight of one bottle cap in ounces
    CAP_WEIGHT_OUNCES = 1 / 7

    # Define the weight of one pound in ounces
    POUND_WEIGHT_OUNCES = 16

    # Define the total weight of Josh's collection in ounces
    collection_weight_ounces = 18 * POUND_WEIGHT_OUNCES

    # Calculate the number of bottle caps in Josh's collection
    num_caps = collection_weight_ounces / CAP_WEIGHT_OUNCES

    # Display the number of bottle caps in Josh's collection
    result = num_caps
    return result

print(solution())