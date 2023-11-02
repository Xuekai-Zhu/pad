def solution():
    # Find the number of teenagers in the children's home
    teenagers = 5 * 6  # the home has five times as many teenagers as toddlers, and there are 6 toddlers

    # Calculate the total number of children in the home
    total_children = 6 + teenagers

    # Find the number of newborns in the home
    newborns = 40 - total_children  # Diana wants to buy winter clothes for all the 40 children in the home

    result = newborns
    return result

print(solution())