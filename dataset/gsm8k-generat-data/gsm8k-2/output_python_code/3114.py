def solution():
    """Susie has 572 beans in the jar. One-fourth of them are red and one-third of the remaining beans are white. Then half of the remaining are green beans. How many green beans are there?"""
    total_beans = 572
    red_beans = total_beans // 4
    remaining_beans = total_beans - red_beans
    white_beans = remaining_beans // 3
    remaining_beans -= white_beans
    green_beans = remaining_beans // 2
    result = green_beans
    return result

print(solution())