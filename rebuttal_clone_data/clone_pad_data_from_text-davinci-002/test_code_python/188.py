def solution():
    """Yesterday, David and William were invited to a party. David broke 2 glasses, while his friend William broke 4 times the number of glasses David broke. How many glasses were broken?"""
    david_glasses = 2
    william_glasses = david_glasses * 4
    total_glasses = david_glasses + william_glasses
    result = total_glasses
    return result

print(solution())