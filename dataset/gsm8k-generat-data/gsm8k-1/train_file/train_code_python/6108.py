def solution():
    """Dr. Harry wants to know how many candies Susan consumed during the week. Susan tells him she bought 3 on Tuesday, 5 on Thursday, 2 on Friday. If she has only 4 of them left, how many did she eat?"""
    candies_bought = 3 + 5 + 2
    candies_left = 4
    candies_consumed = candies_bought - candies_left
    result = candies_consumed
    return result

print(solution())