def solution():
    """A movie theater company is advertising a deal of a movie ticket, a bucket of popcorn, a drink, and a box of candy for $20. Normally, a movie ticket costs $8, a bucket of popcorn costs three dollars less, a drink costs a dollar more than popcorn, and a candy costs half as much as a drink. How many dollars does the deal save a customer who buys a ticket, popcorn, drink, and candy normally?"""
    ticket_price = 8
    popcorn_price = 5
    drink_price = 6
    candy_price = 3
    normal_price = ticket_price + popcorn_price + drink_price + candy_price
    deal_price = 20
    savings = normal_price - deal_price
    result = savings
    return result

print(solution())