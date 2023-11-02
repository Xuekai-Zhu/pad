def solution():
    total_members = 120  # The church has 120 members
    adults = 0.4 * total_members  # 40% of the members are adults
    children = total_members - adults  # The rest are children

    # Calculate how many more children than adults there are
    diff = children - adults
    result = diff
    return result

print(solution())