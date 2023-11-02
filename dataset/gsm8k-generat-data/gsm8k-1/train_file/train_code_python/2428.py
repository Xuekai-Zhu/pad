def solution():
    """Bea and Dawn both have a lemonade stand. Bea sells her lemonade at 25 cents while Dawn sells hers at 28 cents. If Bea sold 10 glasses and Dawn sold 8 glasses, how much more money (in cents) did Bea earn than Dawn?"""
    bea_price = 25
    dawn_price = 28
    bea_sales = 10
    dawn_sales = 8
    bea_earnings = bea_price * bea_sales
    dawn_earnings = dawn_price * dawn_sales
    diff_earnings = bea_earnings - dawn_earnings
    result = diff_earnings
    return result

print(solution())