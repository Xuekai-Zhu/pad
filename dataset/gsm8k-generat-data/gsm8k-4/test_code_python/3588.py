def solution():
    """A group of bedbugs infested an old mattress. Every day, the number of bedbugs would triple. After four days, there were 810 bedbugs burrowing into the mattress. How many bedbugs did the group start with?"""
    # Define the initial number of bedbugs
    bedbugs = None

    # Define the number of days that have passed
    days = 4

    # Define the number of bedbugs after 4 days
    final_bedbugs = 810

    # Calculate the number of bedbugs on the first day
    bedbugs = final_bedbugs / (3 ** days)

    result = int(bedbugs)
    return result

print(solution())