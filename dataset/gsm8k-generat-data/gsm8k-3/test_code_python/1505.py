def solution():
    """Mary had 6 lambs and 2 of the lambs had 2 babies each.  She traded 3 lambs for one goat.  One morning, she woke up and found an extra 7 lambs in the field.  How many lambs does Mary have?"""
    # Initialize the number of lambs
    lambs = 6

    # Add the lambs with babies
    lambs += 2 * 2

    # Trade 3 lambs for a goat
    lambs -= 3
    goats = 1

    # Add the 7 extra lambs
    lambs += 7

    # Return the total number of lambs
    result = lambs
    return result

print(solution())