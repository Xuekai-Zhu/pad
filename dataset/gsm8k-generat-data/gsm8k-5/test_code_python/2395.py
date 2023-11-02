def solution():
    adults = 58
    children = adults - 35 # 35 fewer children than the number of adults
    seniors = 2 * children # twice as many seniors as children

    # Calculate the total number of guests served
    total_guests = adults + children + seniors
    result = total_guests
    return result

print(solution())