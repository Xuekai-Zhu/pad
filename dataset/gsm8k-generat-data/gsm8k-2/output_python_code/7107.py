def solution():
    """As a child, Bobby was able to jump rope 30 times per minute. Now that he is an adult, he can jump 1 jump per second. How many more jumps than when he was a child is Bobby able to jump now that he is an adult?"""
    child_jump_rate = 30
    adult_jump_rate = 60 # 1 jump per second = 60 jumps per minute
    difference = adult_jump_rate - child_jump_rate
    result = difference
    return result

print(solution())