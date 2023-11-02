def solution():
    """A movie theater company is advertising a deal of a movie ticket, a bucket of popcorn, a drink, and a box of candy for $20. Normally, a movie ticket costs $8, a bucket of popcorn costs three dollars less, a drink costs a dollar more than popcorn, and a candy costs half as much as a drink. How many dollars does the deal save a customer who buys a ticket, popcorn, drink, and candy normally?"""
    ticket_cost = 8
    popcorn_cost = 5
    drink_cost = 6
    candy_cost = 3

    normal_cost = ticket_cost + popcorn_cost + drink_cost + candy_cost

    deal_cost = 20

    savings = normal_cost - deal_cost

    result = savings
    return result

print(solution())