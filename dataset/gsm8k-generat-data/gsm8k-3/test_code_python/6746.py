def solution():
    """A club is going to get additional members so that they will have 5 more than twice their current number of their members. If the club has 10 members now, how many additional members do they need?"""
    # Define the current number of club members
    current_members = 10

    # Calculate the number of additional members needed
    additional_members = (2 * current_members) + 5 - current_members

    # Display the number of additional members needed
    result = additional_members
    return result

print(solution())