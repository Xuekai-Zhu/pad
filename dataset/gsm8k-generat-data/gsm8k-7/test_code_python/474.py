def solution():
    num_members = 30

    # Calculate the number of members who ordered lemon juice
    num_lemon_juice = num_members * (2/5)

    # Calculate the remaining number of members
    remaining_members = num_members - num_lemon_juice

    # Calculate the number of members who ordered mango juice
    num_mango_juice = remaining_members * (1/3)

    # Calculate the number of members who ordered orange juice
    num_orange_juice = remaining_members - num_mango_juice

    result = num_orange_juice
    return result

print(solution())