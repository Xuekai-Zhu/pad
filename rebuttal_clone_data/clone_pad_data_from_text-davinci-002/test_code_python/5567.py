def solution():
    initial_beans = 8000
    people = 10
    first_group = 6
    second_group = 4
    first_group_ratio = 2
    last_group_ratio = 1
    last_group_total = 400
    last_group_individual = last_group_total / second_group
    first_group_total = last_group_individual * first_group_ratio * first_group
    total_taken = first_group_total + last_group_total
    beans_left = initial_beans - total_taken
    result = beans_left
    return result

print(solution())