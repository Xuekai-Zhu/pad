def solution():
    # Define the products that Alfa Romeo and Starbucks sell
    alfa_romeo_products = ["automobiles"]
    starbucks_products = ["coffee", "tea", "food", "drink products"]
    # Check if an Alfa Romeo can be ordered at Starbucks
    if "automobiles" in starbucks_products:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())