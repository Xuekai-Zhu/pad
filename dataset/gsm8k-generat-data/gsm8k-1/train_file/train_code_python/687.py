def solution():
    """Trent caught 180 tadpoles then let 75% of them go. How many did he keep?"""
    initial_tadpoles = 180
    percent_left = 25
    tadpoles_left = initial_tadpoles * (percent_left / 100)
    tadpoles_kept = initial_tadpoles - tadpoles_left
    result = tadpoles_kept
    return result

print(solution())