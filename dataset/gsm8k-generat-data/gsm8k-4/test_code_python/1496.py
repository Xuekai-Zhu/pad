def solution():
    """Juniper, the Irish Setter, has 4 bones. Her master gives her enough bones to double her number of bones.
    Unfortunately, the neighbor's dog steals away two of Juniper's bones. How many bones does Juniper have remaining?"""
    # Define the initial number of bones
    initial_bones = 4

    # Double the number of bones
    doubled_bones = initial_bones * 2

    # Subtract the two stolen bones
    bones_remaining = doubled_bones - 2

    result = bones_remaining
    return result

print(solution())