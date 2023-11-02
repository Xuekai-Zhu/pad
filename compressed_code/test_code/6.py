def solution():
    
    initial_weight = 2
    jelly_beans_1 = 2
    brownies = initial_weight * 3 - initial_weight - jelly_beans_1
    jelly_beans_2 = 2
    gummy_worms = (initial_weight + jelly_beans_1 + brownies + jelly_beans_2) * 2 - (initial_weight + jelly_beans_1 + brownies + jelly_beans_2)
    final_weight = initial_weight + jelly_beans_1 + brownies + jelly_beans_2 + gummy_worms
    result = final_weight
    return result

print(solution())