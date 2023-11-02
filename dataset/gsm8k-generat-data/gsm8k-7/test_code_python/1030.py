def solution():
    water_cooler_gallons = 3
    dixie_cup_ounces = 6
    meeting_chairs_per_row = 10
    num_rows = 5
    total_meeting_chairs = meeting_chairs_per_row * num_rows

    # Calculate the total number of ounces of water needed for all cups
    total_water_needed = total_meeting_chairs * dixie_cup_ounces

    # Convert the initial number of gallons to ounces
    initial_water_ounces = water_cooler_gallons * 128

    # Calculate the number of ounces of water left in the cooler
    water_left_ounces = initial_water_ounces - total_water_needed
    result = water_left_ounces
    return result

print(solution())