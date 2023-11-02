def solution():
     total_jelly_beans = 200
     thomas_jelly_beans = total_jelly_beans * 0.1
     remaining_jelly_beans = total_jelly_beans - thomas_jelly_beans
     barry_jelly_beans = remaining_jelly_beans * 0.4
     emmanuel_jelly_beans = remaining_jelly_beans * 0.5
     result = emmanuel_jelly_beans
     return result

print(solution())