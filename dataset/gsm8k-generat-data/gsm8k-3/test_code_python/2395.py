def solution():
    """A chef has served 58 adults, 35 fewer children than the number of adults, and twice as many seniors as children. What is the total number of guests served?"""
    # Define the number of adults served
    adults = 58

    # Calculate the number of children served
    children = adults - 35

    # Calculate the number of seniors served
    seniors = 2 * children

    # Calculate the total number of guests served
    total_guests = adults + children + seniors

    # Display the total number of guests
    result = total_guests
    return result

print(solution())