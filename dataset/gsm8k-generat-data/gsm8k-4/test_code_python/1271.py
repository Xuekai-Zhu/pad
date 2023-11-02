def solution():
    """Dorothy is 15 years old and wants to go to a museum with her family. Her family consists of her, her younger brother, her parents, and her grandfather. The regular ticket cost is $10. People 18 years old or younger have a discount of 30%. How much money will Dorothy have after this trip, when she currently has $70?"""
    
    # Define the ticket price and Dorothy's age
    ticket_price = 10
    dorothy_age = 15
    
    # Calculate the discounted ticket price for Dorothy
    dorothy_ticket_price = ticket_price * 0.7 if dorothy_age <= 18 else ticket_price
    
    # Calculate the total cost of tickets for the family
    total_tickets_cost = dorothy_ticket_price * 4
    
    # Calculate the money Dorothy will have after the trip
    money_after_trip = 70 - total_tickets_cost
    
    return money_after_trip

print(solution())