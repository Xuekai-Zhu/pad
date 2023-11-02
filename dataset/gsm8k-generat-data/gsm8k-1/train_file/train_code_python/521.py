def solution():
    """One barnyard owl makes 5 hoot sounds per minute. If 5 less than 20 hoots per minute are heard coming out of the barn, how many Barnyard owls would this noise be coming from?"""
    hoots_per_minute = 20 - 5
    hoots_per_owl = 5
    owls_needed = hoots_per_minute / hoots_per_owl
    result = owls_needed
    return result

print(solution())