def solution():
    # Determine if the common warthog has tusks that could be used for scrimshaw
    has_tusks = True
    # Determine if the common warthog is hunted for ivory or if it is endangered
    hunted_for_ivory = True
    endangered = False
    # Check if the common warthog could be useful for scrimshaw
    if has_tusks and hunted_for_ivory and not endangered:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())