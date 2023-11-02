def solution():
    """A club with 30 members ordered fruit juices. Two-fifths of them ordered lemon juice. One-third of the remaining members ordered mango juice, and the rest ordered orange juice. How many members ordered orange juice?"""
    total_members = 30
    lemon_juice_members = int(total_members * (2/5))
    remaining_members = total_members - lemon_juice_members
    mango_juice_members = int(remaining_members * (1/3))
    orange_juice_members = remaining_members - mango_juice_members
    result = orange_juice_members
    return result

print(solution())