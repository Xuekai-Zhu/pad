def solution():
    """A club with 30 members ordered fruit juices. Two-fifths of them ordered lemon juice. One-third of the remaining members ordered mango juice, and the rest ordered orange juice.
    How many members ordered orange juice?"""
    total_members = 30
    lemon_juice = (2/5) * total_members
    remaining_members = total_members - lemon_juice
    mango_juice = (1/3) * remaining_members
    orange_juice = remaining_members - mango_juice
    result = orange_juice
    return result

print(solution())