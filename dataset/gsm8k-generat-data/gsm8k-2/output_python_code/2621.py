def solution():
    """Napoleon has 17 jelly beans and Sedrich has 4 more jelly beans than Napoleon. If twice the sum of Napoleon and Sedrich's jelly beans is 4 times the number of jelly beans that Mikey has, how many jelly beans does Mikey have?"""
    napoleon_jelly_beans = 17
    sedrich_jelly_beans = napoleon_jelly_beans + 4
    total_jelly_beans = napoleon_jelly_beans + sedrich_jelly_beans
    mikey_jelly_beans = (total_jelly_beans * 4) / 2
    result = mikey_jelly_beans
    return result

print(solution())