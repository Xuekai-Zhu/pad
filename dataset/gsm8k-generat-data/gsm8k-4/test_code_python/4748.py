def solution():
    """There was some money in the cookie jar. Doris spent $6 from the cookie jar. Martha spent half as much as Doris. If there were $15 left in the cookie jar, how much money, in dollars, was there in the cookie jar at first?"""
    # Initialize the total amount of money in the cookie jar
    total_money = None

    # Subtract Doris' spending from the total
    total_money -= 6

    # Subtract Martha's spending from the total
    martha_spending = 6 / 2
    total_money -= martha_spending

    # The remaining amount should be equal to $15
    # Therefore, we can solve for the initial total money
    total_money += 15

    result = total_money
    return result

print(solution())