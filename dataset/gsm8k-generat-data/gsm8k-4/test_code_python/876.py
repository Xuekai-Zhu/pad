def solution():
    """A choir was singing a song that involved 30 singers. In the first verse, only half of them sang. In the second verse, a third of the remaining singers joined in. How many people joined in the final third verse that the whole choir sang together?"""
    # Define the initial number of singers
    singers = 30

    # Calculate the number of singers who sang in the first verse
    first_verse_singers = singers // 2

    # Calculate the number of singers who performed in the second verse
    second_verse_singers = (singers - first_verse_singers) // 3

    # Calculate the number of singers who performed in the final verse
    final_verse_singers = singers - first_verse_singers - second_verse_singers

    # return the result
    result = final_verse_singers
    return result

print(solution())