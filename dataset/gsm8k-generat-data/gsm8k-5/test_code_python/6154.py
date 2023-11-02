def solution():
    total_characters = 60  # Mary wants to split her 60 characters by their initials

    # Half of the characters have the initial A
    a_initial = total_characters / 2

    # Half of the A_initial characters have the initial C
    c_initial = a_initial / 2

    # The rest of the characters have initials D and E
    d_initial = 2 * (total_characters - a_initial - c_initial) / 3

    result = d_initial
    return result

print(solution())