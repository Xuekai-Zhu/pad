def solution():
    """Yuan is 7 years older than his brother David and twice his age. How old is David?"""
    yuan_age = 2 * david_age
    david_age = yuan_age - 7
    result = david_age
    return result

print(solution())