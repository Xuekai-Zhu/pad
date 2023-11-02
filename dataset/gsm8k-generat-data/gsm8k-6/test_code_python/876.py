def solution():
    # Calculate the number of singers who sang in the first verse
    first_verse_singers = 30 // 2

    # Calculate the number of singers who were left after the first verse
    remaining_singers = 30 - first_verse_singers

    # Calculate the number of singers who joined in the second verse
    second_verse_singers = remaining_singers // 3

    # Calculate the number of singers who sang in the final third verse
    final_verse_singers = first_verse_singers + remaining_singers - second_verse_singers

    result = final_verse_singers
    return result

print(solution())