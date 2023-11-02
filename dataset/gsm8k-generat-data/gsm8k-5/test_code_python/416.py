def solution():
    may_depth = 5  # river is 5 feet deep in mid-May
    june_depth = may_depth + 10  # river is 10 feet deeper in mid-June
    july_depth = june_depth * 3  # river is 3 times deeper in mid-July

    result = july_depth
    return result

print(solution())