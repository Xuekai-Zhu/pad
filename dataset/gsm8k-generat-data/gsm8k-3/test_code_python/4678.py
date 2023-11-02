def solution():
    """A show debut and 200 people buy tickets. For the second showing three times as many people show up. If each ticket cost $25 how much did the show make?"""
    # Define the number of tickets sold for each showing
    tickets_show1 = 200
    tickets_show2 = tickets_show1 * 3

    # Define the cost of each ticket
    ticket_price = 25

    # Compute the total revenue from ticket sales
    total_revenue = (tickets_show1 + tickets_show2) * ticket_price

    # Display the total revenue
    result = total_revenue
    return result

print(solution())