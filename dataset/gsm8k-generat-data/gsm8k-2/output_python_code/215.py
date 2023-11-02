def solution():
    """A church has 120 members. 40% are adults. The rest are children. How many children more children are there than adults?"""
    total_members = 120
    adult_percentage = 0.4
    num_adults = int(total_members * adult_percentage)
    num_children = total_members - num_adults
    diff_children_adults = num_children - num_adults
    result = diff_children_adults
    return result

print(solution())