def solution():
    """Stacy has 32 berries. Steve takes 4 of Stacy's berries, and still has 7 less berries than Stacy started with. How many berries did Steve start with?"""
    # Define the number of berries Stacy started with
    stacy_start = 32

    # Define the number of berries Steve took
    steve_took = 4

    # Define the number of berries Steve had left after taking 4
    steve_left = stacy_start - steve_took - 7

    # Define the number of berries Steve started with
    steve_start = steve_left + steve_took

    result = steve_start
    return result

print(solution())