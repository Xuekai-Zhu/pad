def solution():
    num_panels = 10
    num_sheets_per_panel = 3
    num_beams_per_panel = 2
    num_rods_per_sheet = 10
    num_rods_per_beam = 4

    # Calculate the total number of metal sheets needed
    total_sheets = num_panels * num_sheets_per_panel

    # Calculate the total number of metal beams needed
    total_beams = num_panels * num_beams_per_panel

    # Calculate the total number of metal rods needed for all the sheets
    total_sheet_rods = total_sheets * num_rods_per_sheet

    # Calculate the total number of metal rods needed for all the beams
    total_beam_rods = total_beams * num_rods_per_beam

    # Calculate the total number of metal rods needed for the entire fence
    total_rods = total_sheet_rods + total_beam_rods
    result = total_rods
    return result

print(solution())