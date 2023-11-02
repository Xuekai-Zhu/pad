def solution():
    """Sam, Sid, and Steve brought popsicle sticks for their group activity in their Art class. Sam has thrice as many as Sid, and Sid has twice as many as Steve. If Steve has 12 popsicle sticks, how many popsicle sticks can they use for their Art class activity?"""
    # Define the number of popsicle sticks Steve has
    steve_sticks = 12

    # Calculate the number of sticks Sid has
    sid_sticks = steve_sticks * 2

    # Calculate the number of sticks Sam has
    sam_sticks = sid_sticks * 3

    # Calculate the total number of sticks they have
    total_sticks = steve_sticks + sid_sticks + sam_sticks

    # return the result
    result = total_sticks
    return result

print(solution())