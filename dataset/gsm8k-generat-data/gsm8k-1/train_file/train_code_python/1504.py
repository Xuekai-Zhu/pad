def solution():
    """Mary had 6 lambs and 2 of the lambs had 2 babies each. She traded 3 lambs for one goat. One morning, she woke up and found an extra 7 lambs in the field. How many lambs does Mary have?"""
    initial_lambs = 6
    extra_babies = 2*2
    traded_lambs = 3
    extra_lambs = 7
    current_lambs = initial_lambs + extra_babies - traded_lambs + extra_lambs
    result = current_lambs
    return result

print(solution())