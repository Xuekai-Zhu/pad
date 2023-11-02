def solution():
    total_members = 30  # The club has 30 members
    lemon_juice = (2/5) * total_members  # Two-fifths of the members ordered lemon juice
    remaining_members = total_members - lemon_juice  # Calculate the remaining members
    mango_juice = (1/3) * remaining_members  # One-third of the remaining members ordered mango juice
    orange_juice = remaining_members - mango_juice  # The rest ordered orange juice

    result = orange_juice  # Return the number of members who ordered orange juice
    return result

print(solution())