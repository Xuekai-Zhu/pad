def solution():
    """Adam, Andrew and Ahmed all raise goats. Adam has 7 goats. Andrew has 5 more than twice as many goats as Adam. Ahmed has 6 fewer goats than Andrew. How many goats does Ahmed have?"""
    adam_goats = 7
    andrew_goats = 5 + 2*adam_goats
    ahmed_goats = andrew_goats - 6
    result = ahmed_goats
    return result

print(solution())