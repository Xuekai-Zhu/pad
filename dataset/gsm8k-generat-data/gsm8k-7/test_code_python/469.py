def solution():
    hot_tub_capacity_gallons = 40
    quarts_per_bottle = 1
    quarts_per_gallon = 4
    volume_discount = 0.2  # 20% discount
    bottle_cost = 50

    # Calculate the total number of quarts needed to fill the hot tub
    total_quarts_needed = hot_tub_capacity_gallons * quarts_per_gallon

    # Calculate the total number of bottles needed to fill the hot tub
    total_bottles_needed = total_quarts_needed / quarts_per_bottle

    # Calculate the total cost of all bottles of champagne needed, with volume discount applied
    total_cost = total_bottles_needed * bottle_cost * (1 - volume_discount)
    result = total_cost
    return result

print(solution())