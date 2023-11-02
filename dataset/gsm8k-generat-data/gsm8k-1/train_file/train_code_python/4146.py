def solution():
    """Tom, an avid stamp collector, has 3,000 stamps in his collection. He is very sad because he lost his job last Friday. His brother, Mike, and best friend, Harry, try to cheer him up with more stamps. Harry’s gift to Tom is 10 more stamps than twice Mike’s gift. If Mike has given Tom 17 stamps, how many stamps does Tom’s collection now have?"""
    tom_collection = 3000
    mike_gift = 17
    harry_gift = 2 * mike_gift + 10
    total_gift = mike_gift + harry_gift
    new_collection = tom_collection + total_gift
    result = new_collection
    return result

print(solution())