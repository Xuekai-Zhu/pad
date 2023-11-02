def solution():
    total_jelly_beans = 200
    thomas_share = total_jelly_beans * 0.1

    # Calculate the remaining jelly beans after Thomas takes his share
    remaining_jelly_beans = total_jelly_beans - thomas_share

    # Calculate the total ratio
    total_ratio = 4 + 5

    # Calculate Barry's share using the ratio
    barry_share = remaining_jelly_beans * (4 / total_ratio)

    # Calculate Emmanuel's share using the ratio
    emmanuel_share = remaining_jelly_beans * (5 / total_ratio)

    result = emmanuel_share
    return result

print(solution())