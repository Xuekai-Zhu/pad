def solution():
    """A club is going to get additional members so that they will have 5 more than twice their current number of their members. If the club has 10 members now, how many additional members do they need?"""
    # Define the current number of members
    current_members = 10

    # Calculate the desired number of members based on the given criteria
    desired_members = 5 + 2 * current_members

    # Calculate the number of additional members needed
    additional_members = desired_members - current_members

    # Return the result
    result = additional_members
    return result

print(solution())