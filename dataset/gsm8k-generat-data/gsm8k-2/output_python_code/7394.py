def solution():
    """Matilda has half as many jellybeans as Matt. Matt has ten times as many jellybeans as Steve. If Steve has 84 jellybeans, how many jellybeans does Matilda have?"""
    steve_jellybeans = 84
    matt_jellybeans = 10 * steve_jellybeans
    matilda_jellybeans = matt_jellybeans / 2
    result = matilda_jellybeans
    return result

print(solution())