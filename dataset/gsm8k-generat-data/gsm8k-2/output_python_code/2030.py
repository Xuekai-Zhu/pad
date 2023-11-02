def solution():
    """On a quiz, Martin answered three fewer questions correctly than Kelsey, and Kelsey answered eight more questions correctly than Campbell. If Campbell answered 35 questions correctly, how many did Martin answer correctly?"""
    campbell_correct = 35
    kelsey_correct = campbell_correct + 8
    martin_correct = kelsey_correct - 3
    result = martin_correct
    return result

print(solution())