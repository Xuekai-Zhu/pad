def solution():
    """A group of bedbugs infested an old mattress. Every day, the number of bedbugs would triple. After four days, there were 810 bedbugs burrowing into the mattress. How many bedbugs did the group start with?"""
    # Initialize the number of bedbugs on Day 1 and the number of days
    bedbugs = 1
    days = 4

    # Use a loop to calculate the number of bedbugs after the specified number of days
    for i in range(days):
        bedbugs *= 3

    # Calculate the number of bedbugs that the group started with
    initial_bedbugs = bedbugs / 3

    # Display the initial number of bedbugs
    result = initial_bedbugs
    return result

print(solution())