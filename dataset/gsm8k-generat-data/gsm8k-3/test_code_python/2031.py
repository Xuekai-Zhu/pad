def solution():
    """On a quiz, Martin answered three fewer questions correctly than Kelsey, and Kelsey answered eight more questions correctly than Campbell. If Campbell answered 35 questions correctly, how many did Martin answer correctly?"""
    # Define the number of questions Campbell answered correctly
    campbell_correct = 35

    # Calculate the number of questions Kelsey answered correctly
    kelsey_correct = campbell_correct + 8

    # Calculate the number of questions Martin answered correctly
    martin_correct = kelsey_correct - 3

    # Display the number of questions Martin answered correctly
    result = martin_correct
    return result

print(solution())