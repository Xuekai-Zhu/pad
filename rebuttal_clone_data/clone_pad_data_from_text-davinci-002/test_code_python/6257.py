def solution():
    bags_of_beans_morning = 3
    bags_of_beans_afternoon = 3 * bags_of_beans_morning
    bags_of_beans_evening = 2 * bags_of_beans_morning
    total_use_per_day = bags_of_beans_morning + bags_of_beans_afternoon + bags_of_beans_evening
    total_use_per_week = total_use_per_day * 7
    result = total_use_per_week
    return result

print(solution())