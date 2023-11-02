def solution():
    """To get ready for the new school year, Mary brought her two kids shopping. She bought her son James, a coat for $40 and two pairs of jeans. She bought his sister Jamie, a pair of shoes for $30. The total cost of the items was $110. If the two pairs of jeans for James cost the same price, how much did one pair of jeans cost?"""
    james_coat = 40
    jamie_shoes = 30
    total_cost = 110
    jeans_cost = (total_cost - james_coat - jamie_shoes) / 2
    result = jeans_cost
    return result

print(solution())