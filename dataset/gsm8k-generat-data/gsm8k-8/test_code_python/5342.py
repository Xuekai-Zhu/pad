def solution():
    # Nick hides 10 chocolates
    nick_chocolates = 10

    # Alix hides 3 times as many chocolates as Nick
    alix_chocolates = 3 * nick_chocolates

    # Mom took 5 chocolates from Alix
    alix_chocolates -= 5

    # Calculate how many more chocolates Alix has than Nick
    difference = alix_chocolates - nick_chocolates
    result = difference
    return result

print(solution())