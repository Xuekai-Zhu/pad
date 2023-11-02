def solution():
    """Bridge and Sarah have $3 between them. If Bridget has 50 cents more than Sarah, how many cents does Sarah have?"""
    # Convert $3 to cents
    total_cents = 300

    # Set up equation system
    # b + s = 300
    # b = s + 50
    # Solve for s
    s = (total_cents - 50) / 2

    # Display the number of cents Sarah has
    result = s
    return result

print(solution())