def solution():
    """Tom, an avid stamp collector, has 3,000 stamps in his collection. He is very sad because he lost his job last Friday. His brother, Mike, and best friend, Harry, try to cheer him up with more stamps. Harry’s gift to Tom is 10 more stamps than twice Mike’s gift. If Mike has given Tom 17 stamps, how many stamps does Tom’s collection now have?"""
    tom_stamps = 3000
    mike_stamps = 17
    harry_stamps = 2 * mike_stamps + 10
    total_stamps = tom_stamps + mike_stamps + harry_stamps
    result = total_stamps
    return result

print(solution())