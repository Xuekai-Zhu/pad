def solution():
    """A choir was singing a song that involved 30 singers. In the first verse, only half of them sang. In the second verse, a third of the remaining singers joined in. How many people joined in the final third verse that the whole choir sang together?"""
    initial_singers = 30
    first_verse = initial_singers / 2
    second_verse = (initial_singers - first_verse) / 3
    final_verse = initial_singers - first_verse - second_verse
    result = final_verse
    return result

print(solution())