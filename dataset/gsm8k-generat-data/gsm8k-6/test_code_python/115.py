def solution():
    # Calculate the number of red jelly beans
    coconut_flavored = 750
    red_coconut_flavored = coconut_flavored / 0.25
    red_jelly_beans = red_coconut_flavored / 0.75
    
    # Calculate the total number of jelly beans in the jar
    total_jelly_beans = red_jelly_beans / (3/4)
    result = total_jelly_beans
    
    return result

print(solution())