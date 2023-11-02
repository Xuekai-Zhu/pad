def solution():
    naruto_escaped = True
    temple_of_doom_escape = False  # assuming Naruto was not in the Temple of Doom
    if naruto_escaped and not temple_of_doom_escape:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())