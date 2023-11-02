def solution():
    """A choir was singing a song that involved 30 singers. In the first verse, only half of them sang. In the second verse, a third of the remaining singers joined in. How many people joined in the final third verse that the whole choir sang together?"""
    total_singers = 30
    half_singers = total_singers / 2
    remaining_singers = total_singers - half_singers
    second_verse_singers = remaining_singers / 3
    final_singers = total_singers - half_singers - second_verse_singers
    result = final_singers
    return result

print(solution())