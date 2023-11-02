def solution():
    hoots_per_minute = 20 - 5   # 5 less than 20 hoots per minute
    hoots_per_owl = 5   # one owl makes 5 hoots per minute
    num_owls = hoots_per_minute / hoots_per_owl
    result = num_owls
    return result

print(solution())