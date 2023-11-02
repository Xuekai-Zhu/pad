def solution():
    """Dr. Harry wants to know how many candies Susan consumed during the week. Susan tells him she bought 3 on Tuesday, 5 on Thursday, 2 on Friday. If she has only 4 of them left, how many did she eat?"""
    # Define the number of candies bought on each day
    tuesday_candies = 3
    thursday_candies = 5
    friday_candies = 2

    # Calculate the total number of candies bought
    total_candies_bought = tuesday_candies + thursday_candies + friday_candies

    # Calculate the number of candies Susan ate
    candies_consumed = total_candies_bought - 4

    # Display the number of candies Susan ate
    result = candies_consumed
    return result

print(solution())