def solution():
    total_jelly_beans = 4000
    percent_red = 75
    percent_coconut = 25
    total_red_jelly_beans = total_jelly_beans * (percent_red / 100)
    total_coconut_jelly_beans = total_red_jelly_beans * (percent_coconut / 100)
    result = total_coconut_jelly_beans
    return result

print(solution())