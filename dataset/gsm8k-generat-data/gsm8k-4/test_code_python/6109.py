def solution():
    """Dr. Harry wants to know how many candies Susan consumed during the week. Susan tells him she bought 3 on Tuesday, 5 on Thursday, 2 on Friday. If she has only 4 of them left, how many did she eat?"""
    # Calculate the total number of candies she bought
    total_candies_bought = 3 + 5 + 2 + 4

    # Calculate the number of candies she ate
    candies_ate = total_candies_bought - 4

    # return the result
    result = candies_ate
    return result

print(solution())