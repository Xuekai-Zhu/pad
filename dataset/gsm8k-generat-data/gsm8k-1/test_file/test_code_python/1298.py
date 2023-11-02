def solution():
    """Matthew has a collection of 12 unique toy soldiers. He wants to sell them for a fair price. He found a buyer who is willing to pay for half his collection $5 per toy, and for the other half $7 per toy. If Matthew would agree to that offer, how much money would he earn?"""
    num_toys = 12
    half_toys = num_toys / 2
    price1 = 5
    price2 = 7
    total_price = (half_toys * price1) + (half_toys * price2)
    result = total_price
    return result

print(solution())