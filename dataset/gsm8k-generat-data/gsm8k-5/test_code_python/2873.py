def solution():
    toddlers = 6  # There are 6 toddlers
    teenagers = toddlers * 5  # There are 5 times as many teenagers as toddlers
    children = toddlers + teenagers  # Total number of children
    newborns = 40 - children  # Diana wants to buy clothes for all 40 children, so the rest must be newborns
    result = newborns
    return result

print(solution())