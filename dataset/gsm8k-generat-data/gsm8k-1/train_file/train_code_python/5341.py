def solution():
    """Nick hides 10 chocolates in his closet. His brother Alix hides 3 times as many chocolates than Nick hides. Last night, their mom found and took 5 chocolates from Alix. How many more chocolates does Alix have than Nick?"""
    nick_chocolates = 10
    alix_chocolates = nick_chocolates * 3
    alix_chocolates -= 5
    difference = alix_chocolates - nick_chocolates
    result = difference
    return result

print(solution())