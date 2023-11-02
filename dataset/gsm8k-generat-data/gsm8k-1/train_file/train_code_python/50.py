def solution():
    """Ann is cutting fabric to make curtains. She cuts a 4 foot by 6 foot rectangle for the living room, and a 2 foot by 4 foot rectangle for the bedroom. If the bolt of fabric is 16 feet by 12 feet, how much fabric is left in square feet?"""
    living_room = 4 * 6
    bedroom = 2 * 4
    total_used = living_room + bedroom
    bolt_of_fabric = 16 * 12
    remaining_fabric = bolt_of_fabric - total_used
    result = remaining_fabric
    return result

print(solution())