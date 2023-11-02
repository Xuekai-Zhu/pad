def solution():
    """A house’s living room, dining room and kitchen take up 1,000 sq ft. The house also has a guest bedroom and a master bedroom suite. If the guest bedroom is a quarter of the size of the master bedroom suite, and the house is 2,300 sq ft total, how large is the master bedroom suite?"""
    # Define the size of the living room, dining room, and kitchen
    LIVING_ROOM_SIZE = 200
    DINING_ROOM_SIZE = 250
    KITCHEN_SIZE = 550

    # Calculate the total size of the living room, dining room, and kitchen
    LDK_SIZE = LIVING_ROOM_SIZE + DINING_ROOM_SIZE + KITCHEN_SIZE

    # Calculate the size of the guest bedroom
    GUEST_BEDROOM_SIZE = (2 / 8) * (2300 - LDK_SIZE)

    # Calculate the size of the master bedroom suite
    MASTER_SUITE_SIZE = 2300 - LDK_SIZE - GUEST_BEDROOM_SIZE

    # Display the size of the master bedroom suite
    result = MASTER_SUITE_SIZE
    return result

print(solution())