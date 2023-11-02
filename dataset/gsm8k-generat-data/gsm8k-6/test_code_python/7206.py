def solution():
    # Let x be the total number of chocolates in the box
    # Then (1/2)x have nuts and (1/2)x do not have nuts
    # 80% of (1/2)x have nuts are eaten, so (4/5)(1/2)x have nuts are eaten
    # Half of (1/2)x without nuts are eaten, so (1/4)x without nuts are eaten
    # Therefore, the number of chocolates left is x - (4/5)(1/2)x - (1/4)x = 28
    # Solving for x gives x = 160
    total_chocolates = 160
    result = total_chocolates
    return result

print(solution())