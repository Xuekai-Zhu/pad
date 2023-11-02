def solution():
    """Jolene and Phil have four children, each with the same birthday.  They gave birth to their first child exactly 15 years ago.  They gave birth to their second child exactly one year after the birth of their first child.  They gave birth to their third child on the fourth birthday of their second child. Two years after the birth of their third child, they gave birth to their fourth child.  How old, in years, is their fourth child?"""
    # Calculate the age of the first child
    age_1 = 15

    # Calculate the age of the second child
    age_2 = age_1 + 1

    # Calculate the age of the third child
    age_3 = age_2 + 4

    # Calculate the age of the fourth child
    age_4 = age_3 + 2

    # Display the age of the fourth child
    result = age_4
    return result

print(solution())