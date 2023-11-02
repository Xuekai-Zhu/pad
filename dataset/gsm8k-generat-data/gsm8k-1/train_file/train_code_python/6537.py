def solution():
    """A company is lining a 900-foot path with a fence. Every 6 feet, a fence pole is placed. The entire path is lined with a fence except for a 42-foot bridge. How many fence poles will be placed along the whole path on both sides?"""
    total_path_length = 900
    bridge_length = 42
    fence_length = total_path_length - bridge_length
    fence_pole_spacing = 6
    fence_poles_per_foot = 1 / fence_pole_spacing
    total_fence_poles = fence_poles_per_foot * fence_length * 2
    result = total_fence_poles
    return result

print(solution())