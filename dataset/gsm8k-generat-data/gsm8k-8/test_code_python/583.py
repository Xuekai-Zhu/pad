def solution():
    # Define the leak rates for each hole
    largest_hole_rate = 3
    medium_hole_rate = largest_hole_rate / 2
    smallest_hole_rate = medium_hole_rate / 3

    # Calculate the total amount of water leaked from all three holes in 2 hours
    total_time_in_minutes = 2 * 60
    total_water_leaked = (largest_hole_rate + medium_hole_rate + smallest_hole_rate) * total_time_in_minutes

    result = total_water_leaked
    return result

print(solution())