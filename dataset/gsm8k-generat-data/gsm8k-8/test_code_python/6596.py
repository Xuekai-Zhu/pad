def solution():
    total_jelly_beans = 200
    thomas_share = total_jelly_beans * 0.1
    remaining_jelly_beans = total_jelly_beans - thomas_share
    ratio_total = 4 + 5
    barry_share = (4 / ratio_total) * remaining_jelly_beans
    emmanuel_share = (5 / ratio_total) * remaining_jelly_beans

    result = emmanuel_share
    return result

print(solution())