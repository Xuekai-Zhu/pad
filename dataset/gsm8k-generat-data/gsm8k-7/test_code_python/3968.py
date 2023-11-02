def solution():
    # Let x be the number of brown eggs Linda had originally
    x = 5

    # Since she had three times as many white eggs, she had 3x white eggs
    white_eggs = 3 * x

    # After the accident, she had a total of 5 + 3x + 12 = 3x + 17 eggs
    total_eggs = 3 * x + 17

    # She must have broken total_eggs - 12 eggs
    broken_eggs = total_eggs - 12

    result = broken_eggs
    return result

print(solution())