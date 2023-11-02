def solution():
    """A waterpark opens up and charges $30 for admission. Kids' tickets are half price. If a group of people brings a soda, they can get 20% off the total price of admission. Janet gets tickets for 10 people and 4 of them are children. She buys a soda for $5 to take advantage of the discount for her group. How much did she pay for everything?"""
    adult_ticket_price = 30
    child_ticket_price = 0.5 * adult_ticket_price
    num_adult_tickets = 10 - 4  # 6 adults in the group
    num_child_tickets = 4
    total_price = (adult_ticket_price * num_adult_tickets) + (child_ticket_price * num_child_tickets) + 5
    total_price *= 0.8  # apply 20% discount
    result = total_price
    return result

print(solution())