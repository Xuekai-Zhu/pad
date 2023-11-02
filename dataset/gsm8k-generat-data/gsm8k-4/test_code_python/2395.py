def solution():
    """A chef has served 58 adults, 35 fewer children than the number of adults, and twice as many seniors as children. What is the total number of guests served?"""
    # Define the number of adults
    adults = 58

    # Calculate the number of children
    children = adults - 35

    # Calculate the number of seniors
    seniors = children * 2

    # Calculate the total number of guests served
    total_guests = adults + children + seniors

    # return the result
    result = total_guests
    return result

print(solution())