def solution():
    """A cat spends its time hunting birds. The cat catches 8 birds during the day and twice this many at night. In total, how many birds did the cat catch?"""
    # Calculate the number of birds caught during the day
    day_catch = 8

    # Calculate the number of birds caught at night
    night_catch = day_catch * 2

    # Calculate the total number of birds caught
    total_catch = day_catch + night_catch

    # return the result
    result = total_catch
    return result

print(solution())