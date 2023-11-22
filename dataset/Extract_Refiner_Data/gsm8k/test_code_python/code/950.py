def solution():
    
    # Define the number of measuring spoons and cups
    SPOONS_PER_CUP = 2/3
    CUPS = 2 * 12

    # Calculate the number of measuring spoons and cups
    SPOONS = SPOONS_PER_CUP * CUPS
    CUPS = CUPS * 2

    # Subtract the number of measuring spoons gifted from the total
    SPOONS -= 6

    # Calculate the total number of utensils
    TOTAL_UTENSILS = SPOONS + CUPS

    # Display the total number of utensils
    result = TOTAL_UTENSILS
    return result

print(solution())