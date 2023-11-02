def solution():
    num_children = 39
    monogamy = True
    if num_children > 2 and monogamy:
       result = "yes"
    else:
       result = "no"
    return result

print(solution())