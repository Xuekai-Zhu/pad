def solution():
    """
    Trey is hanging wall decorations around his house. He uses a nail for each of two-thirds of them,
    a thumbtack for each of two-fifths of the rest, and a sticky strip for each of the other decorations.
    He used 15 sticky strips. How many nails did Trey use?
    """
    sticky_strips = 15
    total_decorations = sticky_strips + x + y
    x = (1/3) * total_decorations
    y = (2/5) * ((2/3) * total_decorations)
    nails_used = x
    result = nails_used
    return result

print(solution())