def solution():
    """Diana wants to buy winter clothes for all the 40 children at her local children's home. The home has five times as many teenagers as toddlers. There are also some newborns. If there are 6 toddlers, for how many newborns will Diana be shopping?"""
    toddlers = 6
    teenagers = 5 * toddlers
    total_children = toddlers + teenagers +  # number of newborns
    total_children = 40  # given
    newborns = total_children - toddlers - teenagers
    result = newborns
    return result

print(solution())