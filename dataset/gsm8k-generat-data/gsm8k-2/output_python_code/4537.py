def solution():
    """At the end of a circus act, there are 12 dogs on stage. Half of the dogs are standing on their back legs and the other half are standing on all 4 legs. How many dog paws are on the ground?"""
    back_legs = 6 * 2
    all_legs = 6 * 4
    total_paws = back_legs + all_legs
    result = total_paws
    return result

print(solution())