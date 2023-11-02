def solution():
    """Jenna is buying concert tickets for her group of five friends. She's able to get two of the tickets from the concert website for $50 each before they sell out. A scalper offers to sell her two more tickets for 240% of the normal price, but Jenna convinces him to give her $10 off that total payment. Finally, one of her friends gets a discounted ticket through her job for 60% of the normal price. How much do Jenna's friends pay for their tickets in total?"""
    website_ticket_price = 50
    scalper_ticket_price = website_ticket_price * 2 * 2.4 - 10
    friend_ticket_price = website_ticket_price * 0.6
    total_price = website_ticket_price * 2 + scalper_ticket_price + friend_ticket_price * 2
    result = total_price
    return result

print(solution())