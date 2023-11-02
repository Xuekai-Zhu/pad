def solution():
    """A company is lining a 900-foot path with a fence. Every 6 feet, a fence pole is placed. The entire path is lined with a fence except for a 42-foot bridge. How many fence poles will be placed along the whole path on both sides?"""
    # Define the length of the path and the length of the bridge
    path_length = 900
    bridge_length = 42

    # Calculate the length of the section of the path with a fence
    section_length = path_length - bridge_length

    # Calculate the number of fence poles needed for one side of the path
    fence_poles_one_side = section_length / 6

    # Calculate the total number of fence poles needed for both sides of the path
    fence_poles_both_sides = fence_poles_one_side * 2

    # Display the total number of fence poles needed
    result = fence_poles_both_sides
    return result

print(solution())