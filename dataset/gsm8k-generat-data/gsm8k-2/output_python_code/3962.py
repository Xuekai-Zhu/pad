def solution():
    """9 years from now, John will be 3 times as old as he was 11 years ago. How old is he now?"""
    x = Symbol('x')
    current_age = solve((x+9) - 3*(x-11) - x, x)
    result = current_age[0]
    return result

print(solution())