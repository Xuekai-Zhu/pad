def solution():
    """The movie theater sells matinee tickets for $5, evening tickets for $12, and 3D tickets for $20. If they sell 200 matinee tickets, 300 evening tickets and 100 3D tickets, how much money do they make in total?"""
    # Define the price of each type of ticket
    MATINEE_PRICE = 5
    EVENING_PRICE = 12
    THREE_D_PRICE = 20

    # Define the number of each type of ticket sold
    matinee_tickets = 200
    evening_tickets = 300
    three_d_tickets = 100

    # Calculate the total revenue from matinee tickets
    matinee_revenue = matinee_tickets * MATINEE_PRICE

    # Calculate the total revenue from evening tickets
    evening_revenue = evening_tickets * EVENING_PRICE

    # Calculate the total revenue from 3D tickets
    three_d_revenue = three_d_tickets * THREE_D_PRICE

    # Calculate the total revenue from all ticket sales
    total_revenue = matinee_revenue + evening_revenue + three_d_revenue

    # Display the total revenue
    result = total_revenue
    return result

print(solution())