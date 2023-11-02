def solution():
    
    # Define the cost of the ticket to the amusement park and the selling price per card
    ticket_cost = 100
    selling_price = 1.5

    # Calculate the total revenue from selling the cards
    total_revenue = ticket_cost * selling_price

    # Calculate the number of cards Kenny keeps to sell to the amusement park
    kept_cards = total_revenue / 3

    # Calculate the number of cards Kenny started with
    starting_cards = total_revenue - kept_cards - 50

    # Display the number of cards Kenny started with
    result = starting_cards
    return result

print(solution())