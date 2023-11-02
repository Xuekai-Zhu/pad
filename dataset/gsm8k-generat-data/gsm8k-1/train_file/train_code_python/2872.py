def solution():
    """Diana wants to buy winter clothes for all the 40 children at her local children's home. The home has five times as many teenagers as toddlers. There are also some newborns. If there are 6 toddlers, for how many newborns will Diana be shopping?"""

    total_children = 40
    toddlers = 6
    teenagers = toddlers * 5
    newborns = total_children - (toddlers + teenagers)
    result = newborns

    return result

print(solution())