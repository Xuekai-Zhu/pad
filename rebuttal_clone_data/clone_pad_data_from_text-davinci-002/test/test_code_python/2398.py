def solution():
    fence_panels = 10
    sheets_per_panel = 3
    beams_per_panel = 2
    rods_per_sheet = 10
    rods_per_beam = 4
    total_rods = fence_panels * (sheets_per_panel * rods_per_sheet + beams_per_panel * rods_per_beam)
    result = total_rods
    return result

print(solution())