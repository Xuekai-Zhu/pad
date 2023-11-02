def solution():
    """Elijah drank 8.5 pints of coffee yesterday. Emilio drank 9.5 pints of water yesterday. How many cups of liquid did the two boys drink yesterday?"""
    # Define the amount of liquid in one pint
    PINT_TO_CUP = 2

    # Calculate the total amount of liquid drank by both boys in cups
    total_cups = (8.5 + 9.5) * PINT_TO_CUP

    # Display the total amount of liquid in cups
    result = total_cups
    return result

print(solution())