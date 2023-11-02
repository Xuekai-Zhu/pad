def solution():
    """A church has 120 members. 40% are adults. The rest are children. How many more children are there than adults?"""
    total_members = 120
    percent_adults = 40
    num_adults = total_members * (percent_adults / 100)
    num_children = total_members - num_adults
    difference = num_children - num_adults
    result = difference
    return result

print(solution())