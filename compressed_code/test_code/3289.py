def solution():
    
    num_panels = 10
    num_sheets_per_panel = 3
    num_beams_per_panel = 2
    num_rods_per_sheet = 10
    num_rods_per_beam = 4

    total_sheets = num_panels * num_sheets_per_panel
    total_beams = num_panels * num_beams_per_panel

    total_rods = (total_sheets * num_rods_per_sheet) + (total_beams * num_rods_per_beam)

    result = total_rods
    return result

print(solution())