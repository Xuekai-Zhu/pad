def solution():
    """Jolene and Phil have four children, each with the same birthday. They gave birth to their first child exactly 15 years ago. They gave birth to their second child exactly one year after the birth of their first child. They gave birth to their third child on the fourth birthday of their second child. Two years after the birth of their third child, they gave birth to their fourth child. How old, in years, is their fourth child?"""
    first_child_age = 15
    second_child_age = first_child_age + 1
    third_child_age = second_child_age + 4
    fourth_child_age = third_child_age + 2
    result = fourth_child_age
    return result

print(solution())