def solution():
    """Elijah drank 8.5 pints of coffee yesterday. Emilio drank 9.5 pints of water yesterday. How many cups of liquid did the two boys drink yesterday?"""
    # Define the number of pints in a cup
    PINTS_PER_CUP = 2

    # Convert the number of pints for each person to cups
    elijah_cups = 8.5 * PINTS_PER_CUP
    emilio_cups = 9.5 * PINTS_PER_CUP

    # Calculate the total number of cups consumed
    total_cups = elijah_cups + emilio_cups

    # return the result
    result = total_cups
    return result

print(solution())