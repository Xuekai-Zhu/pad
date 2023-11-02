def solution():
    initial_length = 143  # Tom initially cut the wood to 143 cm
    final_length = initial_length - 25  # Tom cut 25 cm off the board

    # We need to find the length of the original board before 7 cm was cut off
    # x - 7 = final_length (where x is the original length)
    original_length = final_length + 7

    result = original_length
    return result

print(solution())