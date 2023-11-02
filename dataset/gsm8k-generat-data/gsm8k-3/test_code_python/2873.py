def solution():
    """Diana wants to buy winter clothes for all the 40 children at her local children's home. The home has five times as many teenagers as toddlers. There are also some newborns. If there are 6 toddlers, for how many newborns will Diana be shopping?"""
    # Define the number of toddlers and teenagers
    TODDLERS = 6
    TEENAGERS = 5 * TODDLERS

    # Calculate the number of children who are not toddlers or teenagers
    other_children = 40 - TODDLERS - TEENAGERS

    # Since we don't know how many newborns there are, we can use algebra to solve for the number of newborns.
    # The total number of children is 40, so:
    #     toddlers + teenagers + newborns + other_children = 40
    # We already know the values of toddlers and teenagers, and we know the total number of other children:
    #     6 + 5*6 + newborns + other_children = 40
    #     newborns = 40 - 6 - 5*6 - other_children
    # We can substitute the value of other_children we calculated earlier:
    newborns = 40 - TODDLERS - TEENAGERS - other_children

    # Display the number of newborns
    result = newborns
    return result

print(solution())