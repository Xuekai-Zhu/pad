def solution():
    """Ann is cutting fabric to make curtains. She cuts a 4 foot by 6 foot rectangle for the living room, and a 2 foot by 4 foot rectangle for the bedroom. If the bolt of fabric is 16 feet by 12 feet, how much fabric is left in square feet?"""
    # Define the dimensions of the living room and bedroom curtains
    living_room_dim = (4, 6)
    bedroom_dim = (2, 4)

    # Define the dimensions of the bolt of fabric
    bolt_dim = (16, 12)

    # Calculate the total area of fabric used for the curtains
    total_used = sum([dim[0]*dim[1] for dim in [living_room_dim, bedroom_dim]])

    # Calculate the remaining area of fabric on the bolt
    remaining = bolt_dim[0]*bolt_dim[1] - total_used

    # return the result
    result = remaining
    return result

print(solution())