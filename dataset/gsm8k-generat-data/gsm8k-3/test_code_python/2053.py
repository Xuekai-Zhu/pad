def solution():
    """Adam has an orchard. Every day for 30 days he picks 4 apples from his orchard. After a month, Adam has collected all the remaining apples, which were 230. How many apples in total has Adam collected from his orchard?"""
    # Calculate the total number of apples picked in the first 30 days
    apples_picked = 30 * 4

    # Calculate the total number of apples in the orchard before Adam picked any
    total_apples = apples_picked + 230

    # Display the total number of apples collected from the orchard
    result = total_apples
    return result

print(solution())