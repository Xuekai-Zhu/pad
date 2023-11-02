def solution():
    """Jolene and Phil have four children, each with the same birthday. They gave birth to their first child exactly 15 years ago. They gave birth to their second child exactly one year after the birth of their first child. They gave birth to their third child on the fourth birthday of their second child. Two years after the birth of their third child, they gave birth to their fourth child. How old, in years, is their fourth child?"""
    # Calculate the age of the fourth child
    fourth_child_age = 2 + 4 + 1 + 15

    # Return the result
    result = fourth_child_age
    return result

print(solution())