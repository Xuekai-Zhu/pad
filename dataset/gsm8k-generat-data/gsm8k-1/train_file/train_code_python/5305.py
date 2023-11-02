def solution():
    """At the Johnson family reunion, there were 45 children and one third as many adults. One third of the adults wore blue. How many adults did not wear blue?"""
    children = 45
    adults = children * 3
    blue_adults = adults // 3
    non_blue_adults = adults - blue_adults
    result = non_blue_adults
    return result

print(solution())