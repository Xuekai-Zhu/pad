def solution():
    """Yesterday, David and William were invited to a party. David broke 2 glasses, while his friend William broke 4 times the number of glasses David broke. How many glasses were broken?"""
    # Number of glasses David broke
    david_broke = 2

    # Number of glasses William broke
    william_broke = 4 * david_broke

    # Total number of glasses broken
    total_broken = david_broke + william_broke
    result = total_broken
    return result

print(solution())