def solution():
    normal_batch = 1
    quadruple_batch = normal_batch * 4
    can_of_chilis = 1
    two_cans_of_beans = 2
    fifty_percent_more_tomatoes = two_cans_of_beans * 1.5
    total_cans = can_of_chilis + two_cans_of_beans + fifty_percent_more_tomatoes
    quadruple_cans = total_cans * 4
    result = quadruple_cans
    
    return result

print(solution())