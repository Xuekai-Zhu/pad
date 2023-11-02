def solution():
    """A community is building a metal fence. Each fence panel is made of 3 metal sheets, and 2 metal beams. The fence is made of 10 fence panels. If each sheet is made of 10 metal rods and each metal beam is made of 4 metal rods, how many metal rods does the community need for the fence?"""
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