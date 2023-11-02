def solution():
    """John has to restring 3 basses with 4 strings each, twice as many guitars which have 6 strings each, and 3 fewer 8 string guitars than the normal guitars. How many strings does he need?"""
    bass_strings = 3 * 4
    normal_guitars = 2 * bass_strings
    eight_strings_guitars = normal_guitars - 3
    total_strings = bass_strings + normal_guitars * 6 + eight_strings_guitars * 8
    result = total_strings
    return result

print(solution())