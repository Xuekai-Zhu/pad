def solution():
    metal_rods_per_sheet = 10  # Each sheet is made of 10 metal rods
    metal_rods_per_beam = 4  # Each metal beam is made of 4 metal rods
    sheets_per_panel = 3  # Each fence panel is made of 3 metal sheets
    beams_per_panel = 2  # Each fence panel is made of 2 metal beams
    panels = 10  # The fence is made of 10 fence panels

    # Calculate the total number of metal rods needed for the fence
    total_sheets = sheets_per_panel * panels
    total_beams = beams_per_panel * panels
    total_metal_rods = (total_sheets * metal_rods_per_sheet) + (total_beams * metal_rods_per_beam)
    result = total_metal_rods
    return result

print(solution())