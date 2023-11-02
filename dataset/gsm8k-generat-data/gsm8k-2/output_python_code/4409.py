def solution():
    """Bob grew corn in his garden and is ready to harvest it. He has 5 rows of corn, and each row has 80 corn stalks. About every 8 corn stalks will produce a bushel of corn. How many bushels of corn will Bob harvest?"""
    total_stalks = 5 * 80
    bushels = total_stalks // 8
    result = bushels
    return result

print(solution())