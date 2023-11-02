def solution():
    """A waterpark opens up and charges $30 for admission. Kids' tickets are half price. If a group of people brings a soda, they can get 20% off the total price of admission. Janet gets tickets for 10 people and 4 of them are children. She buys a soda for $5 to take advantage of the discount for her group. How much did she pay for everything?"""
    adult_ticket_price = 30
    child_ticket_price = adult_ticket_price / 2
    num_adults = 10 - 4  # Subtracting the 4 children
    num_children = 4
    total_price = (adult_ticket_price * num_adults) + (child_ticket_price * num_children)
    discount = total_price * 0.2 if num_adults + num_children >= 6 else 0
    total_price_with_discount = total_price - discount + 5  # Adding the price of the soda
    result = total_price_with_discount
    return result

print(solution())