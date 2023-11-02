def solution():
    """Juniper, the Irish Setter, has 4 bones. Her master gives her enough bones to double her number of bones. Unfortunately, the neighbor's dog steals away two of Juniper's bones. How many bones does Juniper have remaining?"""
    initial_bones = 4
    doubled_bones = initial_bones * 2
    stolen_bones = 2
    remaining_bones = doubled_bones - stolen_bones
    result = remaining_bones
    return result

print(solution())