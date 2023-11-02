def solution():
    """A club with 30 members ordered fruit juices. Two-fifths of them ordered lemon juice. One-third of the remaining members ordered mango juice, and the rest ordered orange juice. How many members ordered orange juice?"""
    # Define the total number of members
    total_members = 30

    # Calculate the number of members who ordered lemon juice
    lemon_juice_members = int(total_members * (2/5))

    # Calculate the number of remaining members who did not order lemon juice
    remaining_members = total_members - lemon_juice_members

    # Calculate the number of members who ordered mango juice
    mango_juice_members = int(remaining_members * (1/3))

    # Calculate the number of members who ordered orange juice
    orange_juice_members = total_members - lemon_juice_members - mango_juice_members

    # Display the number of members who ordered orange juice
    result = orange_juice_members
    return result

print(solution())