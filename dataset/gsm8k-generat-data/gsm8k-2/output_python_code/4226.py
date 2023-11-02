def solution():
    """A community is building a metal fence. Each fence panel is made of 3 metal sheets, and 2 metal beams. The fence is made of 10 fence panels. If each sheet is made of 10 metal rods and each metal beam is made of 4 metal rods, how many metal rods does the community need for the fence?"""
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