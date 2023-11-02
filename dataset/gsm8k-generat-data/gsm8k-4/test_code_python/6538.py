def solution():
    """A company is lining a 900-foot path with a fence. Every 6 feet, a fence pole is placed. The entire path is lined with a fence except for a 42-foot bridge. How many fence poles will be placed along the whole path on both sides?"""
    # Define the length of the path and the length of the bridge
    path_length = 900
    bridge_length = 42

    # Calculate the length of the fenced portion of the path
    fenced_length = path_length - bridge_length

    # Calculate the number of fence poles needed
    fence_poles = fenced_length // 6

    # Multiply by 2 to account for both sides of the path
    total_fence_poles = fence_poles * 2

    result = total_fence_poles
    return result

print(solution())