def solution():
    """Tomas ate 1.5 pounds of chocolate fudge last week. Katya ate half a pound of peanut butter fudge, while Boris ate 2 pounds of fudge. How many ounces of fudge did the 3 friends eat in total?"""
    # Define the number of ounces in a pound
    OUNCES_PER_POUND = 16

    # Calculate the total number of ounces of fudge eaten
    total_ounces = (1.5 + 0.5 + 2) * OUNCES_PER_POUND

    # Display the total number of ounces
    result = total_ounces
    return result

print(solution())