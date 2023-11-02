def solution():
    # Define the items sold at Home Depot
    home_depot_items = ["hammers", "nails", "wood"]
    # Define the items needed for crucifixion
    crucifixion_supplies = ["nails", "wood"]
    # Check if Home Depot has all the supplies for crucifixion
    if all(item in home_depot_items for item in crucifixion_supplies):
        result = "yes"
    else:
        result = "no"
    return result

print(solution())