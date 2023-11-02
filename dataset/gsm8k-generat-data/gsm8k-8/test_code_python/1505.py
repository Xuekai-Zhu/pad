def solution():
    # Mary starts with 6 lambs
    total_lambs = 6

    # Two of the lambs have 2 babies each
    babies = 2 * 2
    total_lambs += babies

    # She trades 3 lambs for 1 goat
    total_lambs -= 3

    # She wakes up to find 7 more lambs
    total_lambs += 7

    result = total_lambs
    return result

print(solution())