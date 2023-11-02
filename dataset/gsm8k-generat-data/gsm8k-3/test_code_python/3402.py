def solution():
    """A movie theater company is advertising a deal of a movie ticket, a bucket of popcorn, a drink, and a box of candy for $20. Normally, a movie ticket costs $8, a bucket of popcorn costs three dollars less, a drink costs a dollar more than popcorn, and a candy costs half as much as a drink. How many dollars does the deal save a customer who buys a ticket, popcorn, drink, and candy normally?"""
    # Define the regular prices of each item
    TICKET_PRICE = 8
    POPCORN_PRICE = 5
    DRINK_PRICE = 6
    CANDY_PRICE = 3

    # Calculate the regular price of the deal
    regular_price = TICKET_PRICE + POPCORN_PRICE + DRINK_PRICE + CANDY_PRICE

    # Calculate the discounted price of the deal
    discounted_price = 20

    # Calculate the amount saved
    amount_saved = regular_price - discounted_price

    # Display the amount saved
    result = amount_saved
    return result

print(solution())