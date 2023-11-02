def solution():
    """Diana wants to buy winter clothes for all the 40 children at her local children's home. The home has five times as many teenagers as toddlers. There are also some newborns. If there are 6 toddlers, for how many newborns will Diana be shopping?"""
    # Define the number of toddlers and teenagers
    toddlers = 6
    teenagers = toddlers * 5

    # Calculate the number of children that are not toddlers or teenagers
    other_children = 40 - toddlers - teenagers

    # The remaining children will be newborns
    newborns = other_children

    # Return the number of newborns
    result = newborns
    return result

print(solution())