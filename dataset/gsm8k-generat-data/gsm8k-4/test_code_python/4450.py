def solution():
    """Jenna is buying concert tickets for her group of five friends. She's able to get two of the tickets from the concert website for $50 each before they sell out. A scalper offers to sell her two more tickets for 240% of the normal price, but Jenna convinces him to give her $10 off that total payment. Finally, one of her friends gets a discounted ticket through her job for 60% of the normal price. How much do Jenna's friends pay for their tickets in total?"""
    # Define the initial ticket price and the number of tickets purchased
    ticket_price = 50
    num_tickets = 5

    # Calculate the cost of the tickets purchased from the website
    website_cost = ticket_price * 2

    # Calculate the cost of the tickets purchased from the scalper
    scalper_cost = ticket_price * 2 * 2.4 - 10

    # Calculate the cost of the discounted ticket
    discount_cost = ticket_price * 0.6

    # Calculate the total cost
    total_cost = website_cost + scalper_cost + discount_cost

    # Calculate the cost per friend
    cost_per_friend = total_cost / num_tickets

    # return the result
    result = round(cost_per_friend, 2)
    return result

print(solution())