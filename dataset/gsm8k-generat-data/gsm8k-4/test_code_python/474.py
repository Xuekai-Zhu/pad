def solution():
    """A club with 30 members ordered fruit juices. Two-fifths of them ordered lemon juice. One-third of the remaining members ordered mango juice, and the rest ordered orange juice. How many members ordered orange juice?"""
    # Define the initial number of members
    total_members = 30

    # Calculate the number of members who ordered lemon juice
    lemon_members = total_members * 2/5

    # Calculate the number of remaining members
    remaining_members = total_members - lemon_members

    # Calculate the number of members who ordered mango juice
    mango_members = remaining_members * 1/3

    # Calculate the number of members who ordered orange juice
    orange_members = total_members - lemon_members - mango_members

    # return the result
    result = round(orange_members)
    return result

print(solution())