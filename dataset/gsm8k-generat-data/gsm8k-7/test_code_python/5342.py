def solution():
    nick_chocolates = 10
    alix_chocolates = nick_chocolates * 3
    alix_chocolates -= 5  # Mom took 5 chocolates from Alix

    num_more_chocolates = alix_chocolates - nick_chocolates
    result = num_more_chocolates
    return result

print(solution())