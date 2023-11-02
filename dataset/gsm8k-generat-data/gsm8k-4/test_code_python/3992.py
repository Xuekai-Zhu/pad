def solution():
    """Hooper Bay has twice as many pounds of lobster than the two other harbors combined. If the other two harbors have 80 pounds of lobster each, how many pounds of lobster are the three harbors holding?"""
    # Define the total pounds of lobster in the other two harbors
    total_other = 80 + 80

    # Calculate the pounds of lobster in Hooper Bay
    hooper_bay = total_other * 2

    # Calculate the total pounds of lobster in all three harbors
    total_lobster = hooper_bay + total_other

    # Return the result
    result = total_lobster
    return result

print(solution())