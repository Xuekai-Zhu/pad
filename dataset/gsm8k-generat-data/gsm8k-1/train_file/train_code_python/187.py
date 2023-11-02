def solution():
    """Yesterday, David and William were invited to a party. David broke 2 glasses, while his friend William broke 4 times the number of glasses David broke. How many glasses were broken?"""
    glasses_broken_by_david = 2
    glasses_broken_by_william = glasses_broken_by_david * 4
    total_glasses_broken = glasses_broken_by_david + glasses_broken_by_william
    result = total_glasses_broken
    return result

print(solution())