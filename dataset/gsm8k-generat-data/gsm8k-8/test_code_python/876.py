def solution():
    # Define the number of initial singers
    initial_singers = 30

    # Calculate the number of singers in the second verse
    second_verse_singers = (initial_singers / 2) - (initial_singers / 6)

    # Calculate the number of singers in the final verse
    final_singers = initial_singers - second_verse_singers

    result = final_singers
    return result

print(solution())