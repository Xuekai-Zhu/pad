def solution():
    
    total_jelly_beans = 200
    thomas_share = 0.1 * total_jelly_beans
    remaining_jelly_beans = total_jelly_beans - thomas_share
    barry_share = (4 / 9) * remaining_jelly_beans
    emmanuel_share = (5 / 9) * remaining_jelly_beans
    result = emmanuel_share
    return result

print(solution())