def solution():
    """Joel is picking peppers from his garden. He picks 7 on Sunday, 12 on Monday, 14 on Tuesday, 12 on Wednesday, 5 on Thursday, 18 on Friday and 12 on Saturday. 
    He knows that in his garden 20% of the peppers are hot and the rest are not. How many non-hot peppers did he pick?"""
    total_peppers = 7 + 12 + 14 + 12 + 5 + 18 + 12
    hot_peppers = total_peppers * 0.2
    non_hot_peppers = total_peppers - hot_peppers
    result = non_hot_peppers
    return result

print(solution())