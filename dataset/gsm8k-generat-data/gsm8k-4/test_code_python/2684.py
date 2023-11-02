def solution():
    """A state fair charges $5 for a ticket. Two-thirds of the people who buy a ticket will buy deep-fried fair food for $8, one quarter will go on a ride for $4, and one eighth will spend $15 on a souvenir. The fair made $2520 from tickets. How many dollars did they make in all?"""
    # Define the ticket price and the percentages of customers who purchase food, ride, and souvenir
    ticket_price = 5
    food_percent = 2/3
    ride_percent = 1/4
    souvenir_percent = 1/8

    # Calculate the total revenue from ticket sales
    ticket_revenue = 2520

    # Calculate the number of tickets sold
    num_tickets = ticket_revenue / ticket_price

    # Calculate the revenue from food sales
    food_revenue = num_tickets * food_percent * 8

    # Calculate the revenue from ride sales
    ride_revenue = num_tickets * ride_percent * 4

    # Calculate the revenue from souvenir sales
    souvenir_revenue = num_tickets * souvenir_percent * 15

    # Calculate the total revenue
    total_revenue = ticket_revenue + food_revenue + ride_revenue + souvenir_revenue
    
    result = total_revenue
    return result

print(solution())