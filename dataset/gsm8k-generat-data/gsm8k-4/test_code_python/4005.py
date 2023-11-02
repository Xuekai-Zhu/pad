def solution():
    """Shelby had $20 to take to the book fair. She bought one book for $8 and another for $4. She decided to buy as many $4 posters as she could with the money she had left. How many posters can she buy?"""
    # Define the total amount of money Shelby had
    total_money = 20

    # Define the cost of the books she bought
    book1_cost = 8
    book2_cost = 4

    # Calculate the amount of money left after buying the books
    remaining_money = total_money - book1_cost - book2_cost

    # Calculate the number of posters she can buy with the remaining money
    posters_can_buy = remaining_money // 4

    # Return the result
    result = posters_can_buy
    return result

print(solution())