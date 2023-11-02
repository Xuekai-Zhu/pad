def solution():
    """Stacy has 32 berries. Steve takes 4 of Stacy's berries, and still has 7 less berries than Stacy started with. How many berries did Steve start with?"""
    stacy_start = 32
    steve_end = stacy_start - 4
    steve_start = steve_end + 7
    result = steve_start
    return result

print(solution())