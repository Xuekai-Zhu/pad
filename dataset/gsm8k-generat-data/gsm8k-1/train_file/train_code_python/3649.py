def solution():
    """Martin went to a store to buy a new television set. He decided to spend no more than $1,000 and the sales clerk offered him the TV for $100 less and an additional 20% off. How much lower was the price of the television than the amount Martin decided to spend?"""
    max_spending = 1000
    discount = 100
    percent_off = 20
    discounted_price = (max_spending - discount) * (100 - percent_off) / 100
    difference = max_spending - discounted_price
    result = difference
    
    return result

print(solution())