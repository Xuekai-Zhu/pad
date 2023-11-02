def solution():
    """A group of people contains men, women, and children. The number of men is twice the number of women, and the number of women is 3 times the number of children. If the number of children is 30, how many people does this group contain?"""
    children = 30
    women = 3 * children
    men = 2 * women
    total_people = children + women + men
    result = total_people
    return result

print(solution())