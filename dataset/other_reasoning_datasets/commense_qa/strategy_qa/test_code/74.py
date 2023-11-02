def solution():
    japan_bulk_carriers_percentage = 62
    bulk_carrier_hull_material = "steel"
    # Check if the market share of Japanese bulk carriers is relevant to a steel company
    if bulk_carrier_hull_material == "steel" and japan_bulk_carriers_percentage > 50:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())