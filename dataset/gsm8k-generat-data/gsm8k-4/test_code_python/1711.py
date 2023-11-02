def solution():
    """A waterpark opens up and charges $30 for admission. Kids' tickets are half price. If a group of people brings a soda, they can get 20% off the total price of admission. Janet gets tickets for 10 people and 4 of them are children. She buys a soda for $5 to take advantage of the discount for her group. How much did she pay for everything?"""
    # Define the prices of adult and child tickets
    ADULT_TICKET_PRICE = 30
    CHILD_TICKET_PRICE = ADULT_TICKET_PRICE / 2

    # Define the number of adults and children in the group
    num_adults = 10 - 4
    num_children = 4

    # Calculate the total price of tickets before the discount
    total_price_before_discount = (ADULT_TICKET_PRICE * num_adults) + (CHILD_TICKET_PRICE * num_children)

    # Apply the discount for bringing a soda
    total_price_after_discount = total_price_before_discount * 0.8

    # Add the price of the soda
    total_price = total_price_after_discount + 5

    result = total_price
    return result

print(solution())