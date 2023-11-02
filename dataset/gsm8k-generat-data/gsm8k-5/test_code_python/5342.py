def solution():
    nick_chocolates = 10  # Nick hides 10 chocolates
    alix_chocolates = 3 * nick_chocolates  # Alix hides 3 times as many chocolates as Nick

    alix_chocolates -= 5  # Mom took 5 chocolates from Alix

    difference = alix_chocolates - nick_chocolates  # Calculate the difference in the number of chocolates
    result = difference
    return result

print(solution())