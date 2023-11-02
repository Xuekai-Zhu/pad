def solution():
    """Ben has 8 apples more than Phillip does. Tom has three eighths as many apples at Ben has. If Phillip has 40 apples, how many apples does Tom have?"""
    phillip_apples = 40
    ben_apples = phillip_apples + 8
    tom_apples = (3/8) * ben_apples
    result = tom_apples
    return result

print(solution())