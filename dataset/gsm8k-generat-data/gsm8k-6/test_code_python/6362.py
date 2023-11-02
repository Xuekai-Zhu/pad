def solution():
    # Let x be the amount of money Frank had initially
    # Frank spent 1/5 of his money on groceries, leaving him with 4/5 of his money
    # Frank spent 1/4 of the remaining money on a magazine, leaving him with 3/4 of 4/5 of his money
    # 3/4 of 4/5 of x is $360
    x = 360 / (3/4*4/5)
    result = x
    return result

print(solution())