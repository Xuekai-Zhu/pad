def solution():
    total_singers = 30  # There are 30 singers in the choir

    # Calculate the number of singers in the first verse
    first_verse_singers = total_singers // 2

    # Calculate the number of singers remaining after the first verse
    remaining_singers = total_singers - first_verse_singers

    # Calculate the number of singers in the second verse
    second_verse_singers = remaining_singers // 3

    # Calculate the number of singers remaining after the second verse
    remaining_singers -= second_verse_singers

    # Calculate the number of singers in the final verse
    final_verse_singers = remaining_singers

    result = final_verse_singers
    return result

print(solution())