def solution():
    # Calculate the number of children and seniors served
    children = 58 - 35  # 35 fewer children than adults
    seniors = 2 * children  # twice as many seniors as children

    # Calculate the total number of guests served
    total_guests = adults + children + seniors
    result = total_guests
    return result

print(solution())