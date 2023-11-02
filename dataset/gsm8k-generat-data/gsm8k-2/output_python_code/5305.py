def solution():
    """At the Johnson family reunion, there were 45 children and one third as many adults. One third of the adults wore blue. How many adults did not wear blue?"""
    num_children = 45
    num_adults = num_children * 3
    num_blue_adults = num_adults // 3
    num_not_blue_adults = num_adults - num_blue_adults
    result = num_not_blue_adults
    return result

print(solution())