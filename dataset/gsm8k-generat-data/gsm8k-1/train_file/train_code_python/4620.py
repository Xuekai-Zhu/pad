def solution():
    """John has to restring 3 basses with 4 strings each, twice as many guitars which have 6 strings each, and 3 fewer 8 string guitars than the normal guitars. How many strings does he need?"""
    num_basses = 3
    bass_strings = 4
    num_guitars = num_basses * 2
    guitar_strings = 6
    num_8string_guitars = num_guitars - 3
    total_strings = (num_basses * bass_strings) + (num_guitars * guitar_strings) + (num_8string_guitars * 8)
    result = total_strings
    return result

print(solution())