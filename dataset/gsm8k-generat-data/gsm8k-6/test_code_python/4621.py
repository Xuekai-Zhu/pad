def solution():
    # Calculate the total number of strings needed
    bass_strings = 3 * 4  # 3 basses with 4 strings each
    normal_guitar_strings = 2 * 2 * 6  # twice as many guitars with 6 strings each
    eight_string_guitar_strings = (2 * 6 - 3) * 8  # 3 fewer 8 string guitars than the normal guitars, with 8 strings each
    total_strings = bass_strings + normal_guitar_strings + eight_string_guitar_strings

    result = total_strings
    return result

print(solution())