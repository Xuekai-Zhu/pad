def solution():
    # Define the number of adults
    adults = 58

    # Calculate the number of children and seniors
    children = adults - 35
    seniors = 2 * children

    # Calculate the total number of guests
    total_guests = adults + children + seniors

    result = total_guests
    return result

print(solution())