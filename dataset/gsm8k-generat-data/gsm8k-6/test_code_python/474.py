def solution():
    # Find the number of members who ordered lemon juice
    lemon_order = (2/5) * 30

    # Find the number of members who did not order lemon juice
    remaining_members = 30 - lemon_order

    # Find the number of members who ordered mango juice
    mango_order = (1/3) * remaining_members

    # Find the number of members who ordered orange juice
    orange_order = remaining_members - mango_order

    result = orange_order
    return result

print(solution())