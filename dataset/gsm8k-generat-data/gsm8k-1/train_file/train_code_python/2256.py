def solution():
    """There are 4,000 jelly beans in a jar. If three fourths of the jelly beans are red, and one quarter of the red jelly beans are coconut flavored, how many jelly beans are coconut flavored?"""
    total_jelly_beans = 4000
    red_jelly_beans = total_jelly_beans * (3/4)
    coconut_flavored = red_jelly_beans * (1/4)
    
    result = coconut_flavored
    return result

print(solution())