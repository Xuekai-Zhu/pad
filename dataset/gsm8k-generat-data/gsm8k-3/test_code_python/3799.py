def solution():
    """In four years, Suzy will be twice Mary's age then. If Suzy is 20 now, how old is Mary?"""
    # Let Mary's current age be x
    # In four years, Suzy will be 20 + 4 = 24 years old
    # In four years, Mary will be x + 4 years old
    # So, according to the problem, 24 = 2 * (x + 4)

    # Solve for x
    x = (24 - 8) / 2  # x = 8

    # Mary's current age is x years old
    result = x
    return result

print(solution())