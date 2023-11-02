def solution():
    # Calculate the amount of water leaked from the three holes in 2 hours
    largest_hole_rate = 3  # ounces of water leaked per minute from the largest hole
    medium_hole_rate = largest_hole_rate / 2  # ounces of water leaked per minute from the medium-sized hole
    smallest_hole_rate = medium_hole_rate / 3  # ounces of water leaked per minute from the smallest hole
    total_leakage = (largest_hole_rate + medium_hole_rate + smallest_hole_rate) * 2 * 60  # ounces of water leaked in 2 hours
    result = total_leakage
    return result

print(solution())