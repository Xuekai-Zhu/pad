def solution():
    
    sheets_per_panel = 3
    beams_per_panel = 2
    panels = 10
    rods_per_sheet = 10
    rods_per_beam = 4
    
    total_sheets = sheets_per_panel * panels
    total_beams = beams_per_panel * panels
    
    rods_needed_for_sheets = total_sheets * rods_per_sheet
    rods_needed_for_beams = total_beams * rods_per_beam
    
    total_rods = rods_needed_for_sheets + rods_needed_for_beams
    result = total_rods
    
    return result

print(solution())