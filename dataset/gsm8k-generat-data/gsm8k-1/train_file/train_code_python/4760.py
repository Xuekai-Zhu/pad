def solution():
    """There are 100 jellybeans in a glass jar. Mrs. Copper’s kindergarten class normally has 24 kids, but 2 children called in sick and stayed home that day. The remaining children who attended school eat 3 jellybeans each. How many jellybeans are still left in the jar?"""
    num_jellybeans = 100
    num_kids_present = 22
    num_jellybeans_eaten = num_kids_present * 3
    num_jellybeans_left = num_jellybeans - num_jellybeans_eaten
    result = num_jellybeans_left
    return result

print(solution())