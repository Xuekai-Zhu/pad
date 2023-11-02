def solution():
    """Before he lost one, Policeman O'Brien had 5 more than twice as many hats as fire chief Simpson. If fire chief Simpson has 15 hats, how many hats does Policeman O'Brien now have?"""
    simpson_hats = 15
    obrien_hats = 5 + 2 * simpson_hats - 1
    result = obrien_hats
    return result

print(solution())