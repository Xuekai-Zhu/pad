def solution():
    """Kimmie received $450 from her handmade crafts at the supermarket. Her friend Zahra received 1/3 less money when she sold the same amount of handmade crafts at Etsy. If both of them save half of their earnings on the same savings account, calculate the total amount of money in the joint savings account?"""

    kimmie_earnings = 450
    zahra_earnings = kimmie_earnings - (1/3 * kimmie_earnings)
    total_earnings = kimmie_earnings + zahra_earnings

    savings_account = total_earnings / 2

    result = savings_account

    return result

print(solution())