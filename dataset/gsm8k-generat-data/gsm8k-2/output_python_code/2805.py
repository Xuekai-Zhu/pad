def solution():
    """John buys 4 pounds of beef. He uses all but 1 pound in soup. He uses twice as many pounds of vegetables as beef. How many pounds of vegetables did he use?"""
    beef = 4
    beef_used = beef - 1
    vegetables = 2 * beef_used
    result = vegetables
    return result

print(solution())