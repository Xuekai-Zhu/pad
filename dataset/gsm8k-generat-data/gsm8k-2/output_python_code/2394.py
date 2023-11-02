def solution():
    """A chef has served 58 adults, 35 fewer children than the number of adults, and twice as many seniors as children. What is the total number of guests served?"""
    adults = 58
    children = adults - 35
    seniors = 2 * children
    total_guests = adults + children + seniors
    result = total_guests
    return result

print(solution())