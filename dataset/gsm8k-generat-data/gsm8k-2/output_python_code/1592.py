def solution():
    """Yun had 20 paperclips initially, but then lost 12. Marion has 1/4 more than what Yun currently has, plus 7. How many paperclips does Marion have?"""
    yun_paperclips = 20 - 12
    marion_paperclips = yun_paperclips * 1.25 + 7
    result = marion_paperclips
    return result

print(solution())