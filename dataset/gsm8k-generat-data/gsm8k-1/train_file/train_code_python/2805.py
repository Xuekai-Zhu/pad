def solution():
    """John buys 4 pounds of beef. He uses all but 1 pound in soup. He uses twice as many pounds of vegetables as beef. How many pounds of vegetables did he use?"""
    pounds_of_beef = 4
    pounds_of_vegetables = 2 * (pounds_of_beef - 1)
    result = pounds_of_vegetables
    return result

print(solution())