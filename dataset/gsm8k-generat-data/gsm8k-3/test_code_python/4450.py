def solution():
    """Jenna is buying concert tickets for her group of five friends. She's able to get two of the tickets from the concert website for $50 each before they sell out. A scalper offers to sell her two more tickets for 240% of the normal price, but Jenna convinces him to give her $10 off that total payment. Finally, one of her friends gets a discounted ticket through her job for 60% of the normal price. How much do Jenna's friends pay for their tickets in total?"""
    # Calculate the cost of the two tickets bought from the concert website
    web_tickets = 2
    web_ticket_price = 50
    web_cost = web_tickets * web_ticket_price

    # Calculate the cost of the two tickets bought from the scalper
    scalper_tickets = 2
    scalper_ticket_price = web_ticket_price * 2.4
    scalper_discount = 10
    scalper_cost = scalper_tickets * scalper_ticket_price - scalper_discount

    # Calculate the cost of the discounted ticket bought by Jenna's friend
    friend_discount = 0.6
    friend_ticket_price = web_ticket_price
    friend_cost = friend_ticket_price * friend_discount

    # Calculate the total cost for all the tickets
    total_cost = web_cost + scalper_cost + friend_cost

    # Calculate the cost per person (assuming everyone pays the same amount)
    per_person_cost = total_cost / 5

    # Display the cost per person
    result = per_person_cost
    return result

print(solution())