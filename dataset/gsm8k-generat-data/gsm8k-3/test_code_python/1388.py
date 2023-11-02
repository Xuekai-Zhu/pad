def solution():
    """Sami finds 3 spiders in the playground. Hunter sees 12 ants climbing the wall. Ming discovers 8 ladybugs in the sandbox, and watches 2 of them fly away. How many insects are remaining in the playground?"""
    # Calculate the total number of insects
    total_insects = 3 + 12 + 8

    # Calculate the number of ladybugs remaining
    remaining_ladybugs = 8 - 2

    # Calculate the total number of remaining insects
    remaining_insects = total_insects - 2

    # Display the total number of remaining insects in the playground
    result = remaining_insects
    return result

print(solution())