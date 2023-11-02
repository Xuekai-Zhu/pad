def solution():
    """A community is building a metal fence. Each fence panel is made of 3 metal sheets, and 2 metal beams. The fence is made of 10 fence panels. If each sheet is made of 10 metal rods and each metal beam is made of 4 metal rods, how many metal rods does the community need for the fence?"""
    # Define the number of fence panels and the number of metal sheets and beams in each panel
    fence_panels = 10
    sheets_per_panel = 3
    beams_per_panel = 2

    # Define the number of metal rods in each sheet and beam
    rods_per_sheet = 10
    rods_per_beam = 4

    # Calculate the total number of metal sheets and beams needed for the fence
    total_sheets = fence_panels * sheets_per_panel
    total_beams = fence_panels * beams_per_panel

    # Calculate the total number of metal rods needed for the fence
    total_rods = (total_sheets * rods_per_sheet) + (total_beams * rods_per_beam)

    # return the result
    result = total_rods
    return result

print(solution())