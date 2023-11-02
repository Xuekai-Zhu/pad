def solution():
    """A company is lining a 900-foot path with a fence. Every 6 feet, a fence pole is placed. The entire path is lined with a fence except for a 42-foot bridge. How many fence poles will be placed along the whole path on both sides?"""
    path_length = 900
    pole_spacing = 6
    bridge_length = 42
    fenced_path_length = path_length - bridge_length
    poles_per_side = (fenced_path_length // pole_spacing) + 1  # Add 1 for the first pole
    total_poles = 2 * poles_per_side
    result = total_poles
    return result

print(solution())