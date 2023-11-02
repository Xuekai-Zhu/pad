def solution():
    """Jolene and Phil have four children, each with the same birthday. They gave birth to their first child exactly 15 years ago. They gave birth to their second child exactly one year after the birth of their first child. They gave birth to their third child on the fourth birthday of their second child. Two years after the birth of their third child, they gave birth to their fourth child. How old, in years, is their fourth child?"""
    age_one_child = 15
    age_two_children = 1 + age_one_child
    age_three_children = 4 + age_two_children
    age_four_children = 2 + age_three_children
    result = age_four_children
    return result

print(solution())