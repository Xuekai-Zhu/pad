def solution():
    space_mountain = "Disney"
    bugs_bunny = "Warner Bros."
    six_flags = "Six Flags"
    if bugs_bunny in six_flags and space_mountain in Disney:
        result = "no"
    else:
        result = "cannot determine"
    return result

print(solution())