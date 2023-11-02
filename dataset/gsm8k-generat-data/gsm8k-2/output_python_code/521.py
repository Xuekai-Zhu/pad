def solution():
    """One barnyard owl makes 5 hoot sounds per minute. If 5 less than 20 hoots per minute are heard coming out of the barn, how many Barnyard owls would this noise be coming from?"""
    hoots_per_minute = 20
    owl_hoots_per_minute = 5
    total_owls = (hoots_per_minute - 5) / owl_hoots_per_minute
    result = total_owls
    return result

print(solution())