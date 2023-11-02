def solution():
    """Hooper Bay has twice as many pounds of lobster than the two other harbors combined. If the other two harbors have 80 pounds of lobster each, how many pounds of lobster are the three harbors holding?"""
    # Calculate the total pounds of lobster in the other two harbors combined
    other_harbors = 80 * 2

    # Calculate the amount of lobster in Hooper Bay
    hooper_bay = other_harbors * 2

    # Calculate the total pounds of lobster in all three harbors
    total = other_harbors + hooper_bay

    # Display the total pounds of lobster
    result = total
    return result

print(solution())