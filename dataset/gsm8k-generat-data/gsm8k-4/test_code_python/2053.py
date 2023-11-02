def solution():
    """Adam has an orchard. Every day for 30 days he picks 4 apples from his orchard. After a month, Adam has collected all the remaining apples, which were 230. How many apples in total has Adam collected from his orchard?"""
    # Calculate the total number of apples picked by Adam during the 30 days
    total_picked = 30 * 4

    # Calculate the total number of apples in Adam's orchard before he picked them
    total_orchard = total_picked + 230

    # return the result
    result = total_orchard
    return result

print(solution())