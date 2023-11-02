def solution():
    """Barry, Thomas and Emmanuel are to share a jar of 200 jelly beans. If Thomas takes 10%, and Barry and Emmanuel are to share the remainder in the ratio 4:5 respectively, how many jelly beans will Emmanuel get?"""
    total_jelly_beans = 200
    thomas_share = 0.1 * total_jelly_beans
    remaining_jelly_beans = total_jelly_beans - thomas_share
    barry_share = (4 / 9) * remaining_jelly_beans
    emmanuel_share = (5 / 9) * remaining_jelly_beans
    result = emmanuel_share
    return result

print(solution())