def solution():
    total_homes = 20  # Faith's neighborhood has 20 homes
    panels_per_home = 10  # Each home needs 10 solar panels
    total_panels = total_homes * panels_per_home  # Total number of solar panels required
    supplier_panels = total_panels - 50  # The supplier brought 50 panels less than required
    homes_with_panels = supplier_panels // panels_per_home  # Calculate the number of homes with solar panels

    result = homes_with_panels
    return result

print(solution())