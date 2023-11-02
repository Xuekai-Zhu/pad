def solution():
    """A club is going to get additional members so that they will have 5 more than twice their current number of their members. If the club has 10 members now, how many additional members do they need?"""
    current_members = 10
    desired_members = 5 + (2 * current_members)
    additional_members = desired_members - current_members
    result = additional_members
    return result

print(solution())