def solution():
    num_singers = 30

    # Calculate the number of singers who sang in the first verse
    num_first_verse_singers = num_singers / 2

    # Calculate the number of singers who were remaining after the first verse
    num_remaining_singers = num_singers - num_first_verse_singers

    # Calculate the number of singers who joined in the second verse
    num_second_verse_singers = num_remaining_singers / 3

    # Calculate the number of singers who sang in the final third verse
    num_final_verse_singers = num_singers - num_first_verse_singers - num_second_verse_singers
    result = num_final_verse_singers
    return result

print(solution())