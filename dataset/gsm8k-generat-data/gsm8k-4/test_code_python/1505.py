def solution():
    """Mary had 6 lambs and 2 of the lambs had 2 babies each. She traded 3 lambs for one goat. One morning, she woke up and found an extra 7 lambs in the field. How many lambs does Mary have?"""
    # Mary's initial number of lambs
    initial_lambs = 6

    # Two of the lambs had 2 babies each
    initial_lambs += 2*2

    # Mary traded 3 lambs for one goat
    initial_lambs -= 3

    # Mary found an extra 7 lambs in the field
    final_lambs = initial_lambs + 7

    # return the result
    result = final_lambs
    return result

print(solution())