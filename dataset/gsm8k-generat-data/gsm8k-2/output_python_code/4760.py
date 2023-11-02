def solution():
    """There are 100 jellybeans in a glass jar. Mrs. Copper’s kindergarten class normally has 24 kids, but 2 children called in sick and stayed home that day. The remaining children who attended school eat 3 jellybeans each. How many jellybeans are still left in the jar?"""
    jellybean_count = 100
    attending_kids = 22
    eaten_jellybeans = attending_kids * 3
    remaining_jellybeans = jellybean_count - eaten_jellybeans
    result = remaining_jellybeans
    return result

print(solution())