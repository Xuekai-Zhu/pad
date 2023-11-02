def solution():
    """Juniper, the Irish Setter, has 4 bones. Her master gives her enough bones to double her number of bones. Unfortunately, the neighbor's dog steals away two of Juniper's bones.  How many bones does Juniper have remaining?"""
    # Define Juniper's initial number of bones
    initial_bones = 4

    # Double Juniper's number of bones
    doubled_bones = initial_bones * 2

    # Subtract the 2 stolen bones
    remaining_bones = doubled_bones - 2

    # Display the number of remaining bones
    result = remaining_bones
    return result

print(solution())