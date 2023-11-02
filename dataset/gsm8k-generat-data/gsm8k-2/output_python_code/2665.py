def solution():
    """If Jim has 20 apples, and Jane has 60 apples, and Jerry has 40 apples, how many times can Jim's number of apples fit into the average amount of apples for a person in the group?"""
    total_apples = 20 + 60 + 40
    average_apples = total_apples / 3
    jim_ratio = 20 / average_apples
    result = jim_ratio
    return result

print(solution())