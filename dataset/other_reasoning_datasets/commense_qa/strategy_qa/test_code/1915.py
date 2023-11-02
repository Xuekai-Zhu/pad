def solution():
    sonnet_lines = 14
    jabberwocky_lines = 28
    if jabberwocky_lines % sonnet_lines == 0:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())