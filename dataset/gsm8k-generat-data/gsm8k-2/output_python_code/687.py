def solution():
    """Trent caught 180 tadpoles then let 75% of them go. How many did he keep?"""
    total_tadpoles = 180
    released_tadpoles = total_tadpoles * 0.75
    kept_tadpoles = total_tadpoles - released_tadpoles
    result = kept_tadpoles
    return result

print(solution())