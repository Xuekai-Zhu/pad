def solution():
    """Barry, Thomas and Emmanuel are to share a jar of 200 jelly beans. If Thomas takes 10%, and Barry and Emmanuel are to share the remainder in the ratio 4:5 respectively, how many jelly beans will Emmanuel get?"""
    total_jelly_beans = 200
    thomas_share = total_jelly_beans * 0.1
    remainder = total_jelly_beans - thomas_share
    total_ratio = 4+5
    emmanuel_ratio = 5
    emmanuel_share = (emmanuel_ratio / total_ratio) * remainder
    result = emmanuel_share
    return result

print(solution())