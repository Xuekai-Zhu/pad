def solution():
    # Define the given values
    total_cost = 55
    shrimp_trays = 5
    shrimp_tray_price = 5
    gum_packs = 2
    yogurt_pints = 5
    gum_price = 0.5 * yogurt_pints

    # Calculate the total cost of the yogurt pints
    yogurt_price = (total_cost - (shrimp_trays * shrimp_tray_price) - (gum_packs * gum_price)) / yogurt_pints
    result = yogurt_price
    return result

print(solution())