def solution():
    """Kimmie received $450 from her handmade crafts at the supermarket. Her friend Zahra received 1/3 less money when she sold the same amount of handmade crafts at Etsy. If both of them save half of their earnings on the same savings account, calculate the total amount of money in the joint savings account?"""
    # Calculate the amount of money Zahra received
    zahra_money = 450 * (2/3)

    # Calculate the total amount of money earned from selling handmade crafts
    total_money = 450 + zahra_money

    # Calculate the amount of money saved by each of them
    kimmie_savings = 450 * 0.5
    zahra_savings = zahra_money * 0.5

    # Calculate the total amount of money in the joint savings account
    total_savings = kimmie_savings + zahra_savings

    # return the result
    result = total_savings
    return result

print(solution())