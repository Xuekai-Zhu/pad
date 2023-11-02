def solution():
    """A performing magician has a disappearing act where he makes a random member of his audience disappear and reappear. Unfortunately, one-tenth of the time, the audience member never reappears. However, one-fifth of the time, two people reappear instead of only one. If the magician has put on 100 performances of the act this year, how many people have reappeared?"""
    performances = 100
    total_people_disappeared = performances
    never_reappeared = total_people_disappeared * 0.1
    two_people_reappeared = total_people_disappeared * 0.2
    one_person_reappeared = total_people_disappeared - never_reappeared - two_people_reappeared
    total_people_reappeared = one_person_reappeared + (2 * two_people_reappeared)
    result = total_people_reappeared
    
    return result

print(solution())