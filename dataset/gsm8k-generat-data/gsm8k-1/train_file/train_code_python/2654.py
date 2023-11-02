def solution():
    """Trey is hanging wall decorations around his house. He uses a nail for each of two-thirds of them, a thumbtack for each of two-fifths of the rest, and a sticky strip for each of the other decorations. He used 15 sticky strips. How many nails did Trey use?"""
    total_decorations = 15 + (15 * 5 / 3) + (15 * 3 / 5)
    nails_used = total_decorations * 2 / 3
    result = nails_used
    return result

print(solution())