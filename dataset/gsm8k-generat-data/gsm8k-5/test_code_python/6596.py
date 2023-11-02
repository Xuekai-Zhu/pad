def solution():
    total_jelly_beans = 200  # There are 200 jelly beans in the jar
    thomas_share = 0.1 * total_jelly_beans  # Thomas takes 10% of the jelly beans
    remaining_jelly_beans = total_jelly_beans - thomas_share  # The remaining jelly beans are to be shared by Barry and Emmanuel

    # Calculate Barry's share of the remaining jelly beans
    barry_share = (4 / 9) * remaining_jelly_beans

    # Calculate Emmanuel's share of the remaining jelly beans
    emmanuel_share = (5 / 9) * remaining_jelly_beans

    result = emmanuel_share
    return result

print(solution())