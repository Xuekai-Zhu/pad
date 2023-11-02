def solution():
    """Maggie went to Lou's aquarium and saw 100 goldfish in the aquarium. She asked if she could take some home to care for, and she was allowed to catch half of them. While using a catching net, she caught 3/5 of the total number of goldfish she was allowed to take home. How many goldfish does Maggie remain with to catch to get the total number she was allowed to take home?"""
    total_goldfish = 100
    allowed_goldfish = total_goldfish / 2
    caught_goldfish = 3/5 * allowed_goldfish
    remaining_goldfish = allowed_goldfish - caught_goldfish
    result = remaining_goldfish
    return result

print(solution())