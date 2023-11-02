def solution():
    """By the time Anne is two times as old as Emile, Emile will be six times as old as Maude. If Maude will be 8 years old, how old will Anne be?"""
    # Define Maude's age
    maude_age = 8

    # Calculate Emile's age
    emile_age = maude_age * 6 / 1

    # Calculate Anne's age
    anne_age = emile_age * 2

    # Display Anne's age
    result = anne_age
    return result

print(solution())