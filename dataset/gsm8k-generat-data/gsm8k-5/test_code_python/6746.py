def solution():
    current_members = 10  # The club currently has 10 members
    additional_members = (2 * current_members) + 5  # The club needs 5 more than twice their current number of members
    required_members = additional_members - current_members  # The club needs to get this many additional members

    result = required_members
    return result

print(solution())