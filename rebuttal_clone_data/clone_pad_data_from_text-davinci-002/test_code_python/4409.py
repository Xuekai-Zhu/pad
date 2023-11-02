def solution():
    cases_of_beans = 15
    tins_per_case = 24
    percentage_damaged = 5
    tins_damaged = cases_of_beans * tins_per_case * (percentage_damaged / 100)
    tins_left = cases_of_beans * tins_per_case - tins_damaged
    result = tins_left
    return result

print(solution())