def solution():
    """Joshua collected 80 rocks while Jose collected 14 fewer rocks. Albert has collected 20 more rocks than Jose. How many more rocks did Albert collect than Joshua?"""
    joshua_rocks = 80
    jose_rocks = joshua_rocks - 14
    albert_rocks = jose_rocks + 20
    difference = albert_rocks - joshua_rocks
    result = difference
    return result

print(solution())