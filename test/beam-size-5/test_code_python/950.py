def solution():
    
    # Define the number of measuring cups Jonathan has
    cups = 2 * 12

    # Calculate the number of measuring spoons Jonathan has
    spoons = cups * (2/3)

    # Calculate the number of utensils Jonathan has remaining
    utensils_remaining = spoons - 6

    # Display the number of utensils Jonathan has remaining
    result = utensils_remaining
    return result

print(solution())