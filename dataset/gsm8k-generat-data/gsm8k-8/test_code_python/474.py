def solution():
    # Calculate the number of members who ordered lemon juice
    lemon_order = 30 * (2/5)

    # Calculate the number of remaining members after lemon juice order
    remaining_members = 30 - lemon_order

    # Calculate the number of members who ordered mango juice
    mango_order = remaining_members * (1/3)

    # Calculate the number of members who ordered orange juice
    orange_order = remaining_members - mango_order

    result = orange_order
    return result

print(solution())