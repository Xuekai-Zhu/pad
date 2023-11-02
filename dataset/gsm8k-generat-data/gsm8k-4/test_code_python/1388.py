def solution():
    """Sami finds 3 spiders in the playground. Hunter sees 12 ants climbing the wall. Ming discovers 8 ladybugs in the sandbox, and watches 2 of them fly away. How many insects are remaining in the playground?"""
    # Define the initial numbers of spiders, ants, and ladybugs
    spiders = 3
    ants = 12
    ladybugs = 8

    # Subtract the number of ladybugs that flew away
    ladybugs -= 2

    # Calculate the remaining number of insects
    remaining_insects = spiders + ants + ladybugs

    # Return the result
    result = remaining_insects
    return result

print(solution())