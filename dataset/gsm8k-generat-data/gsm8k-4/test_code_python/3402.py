def solution():
    """A movie theater company is advertising a deal of a movie ticket, a bucket of popcorn, a drink, and a box of candy for $20. Normally, a movie ticket costs $8, a bucket of popcorn costs three dollars less, a drink costs a dollar more than popcorn, and a candy costs half as much as a drink. How many dollars does the deal save a customer who buys a ticket, popcorn, drink, and candy normally?"""
    # Define the normal prices of each item
    normal_ticket_price = 8
    normal_popcorn_price = normal_ticket_price - 3
    normal_drink_price = normal_popcorn_price + 1
    normal_candy_price = normal_drink_price / 2

    # Calculate the normal price of buying all four items separately
    normal_price = normal_ticket_price + normal_popcorn_price + normal_drink_price + normal_candy_price

    # Calculate the amount saved by buying the deal
    savings = normal_price - 20
    result = savings
    return result

print(solution())