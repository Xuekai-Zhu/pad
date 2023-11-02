def solution():
    """A choir was singing a song that involved 30 singers. In the first verse, only half of them sang. In the second verse, a third of the remaining singers joined in. How many people joined in the final third verse that the whole choir sang together?"""
    # Define the number of singers in the choir and initialize the number of singers in the first and second verses
    total_singers = 30
    singers_first_verse = total_singers // 2
    singers_second_verse = 0

    # Calculate the number of singers in the second verse
    singers_remaining = total_singers - singers_first_verse
    singers_second_verse = singers_remaining // 3

    # Calculate the number of singers in the final third verse
    singers_final_verse = total_singers - singers_first_verse - singers_second_verse

    # Display the number of singers in the final third verse
    result = singers_final_verse
    return result

print(solution())