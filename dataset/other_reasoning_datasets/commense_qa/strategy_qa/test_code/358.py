def solution():
    intel_products = ["processors", "chipsets", "GPUs"]
    mcdonalds_products = ["food", "beverages"]
    overlap = [product for product in intel_products if product in mcdonalds_products]
    if overlap:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())