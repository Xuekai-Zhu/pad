def solution():
    """Bea and Dawn both have a lemonade stand. Bea sells her lemonade at 25 cents while Dawn sells hers at 28 cents. If Bea sold 10 glasses and Dawn sold 8 glasses, how much more money (in cents) did Bea earn than Dawn?"""
    bea_price = 25
    dawn_price = 28
    bea_glasses_sold = 10
    dawn_glasses_sold = 8
    bea_earnings = bea_price * bea_glasses_sold
    dawn_earnings = dawn_price * dawn_glasses_sold
    difference = bea_earnings - dawn_earnings
    result = difference
    return result

print(solution())