def solution():
    # Define the number of sheets and beams per panel
    sheets_per_panel = 3
    beams_per_panel = 2

    # Define the number of panels in the fence
    number_of_panels = 10

    # Define the number of rods per sheet and beam
    rods_per_sheet = 10
    rods_per_beam = 4

    # Calculate the total number of rods needed for the fence
    total_rods = (sheets_per_panel * rods_per_sheet + beams_per_panel * rods_per_beam) * number_of_panels
    result = total_rods
    return result

print(solution())