def solution():
    """A movie theater charges $5 for matinee tickets, $7 for evening tickets, and $10 for opening night tickets. A bucket of popcorn costs $10. On Friday, they had 32 matinee customers, 40 evening customers, and 58 customers for an opening night showing of a movie. If half the customers bought popcorn, how much money in dollars did the theater make on Friday night?"""
    # Define the prices of different types of tickets and popcorn
    matinee_ticket_price = 5
    evening_ticket_price = 7
    opening_night_ticket_price = 10
    popcorn_price = 10

    # Count the number of customers for each type of ticket
    matinee_customers = 32
    evening_customers = 40
    opening_night_customers = 58

    # Calculate the total revenue from ticket sales
    matinee_revenue = matinee_customers * matinee_ticket_price
    evening_revenue = evening_customers * evening_ticket_price
    opening_night_revenue = opening_night_customers * opening_night_ticket_price
    total_ticket_revenue = matinee_revenue + evening_revenue + opening_night_revenue

    # Calculate the total revenue from popcorn sales
    total_customers = matinee_customers + evening_customers + opening_night_customers
    popcorn_customers = total_customers / 2
    total_popcorn_revenue = popcorn_customers * popcorn_price

    # Add the revenue from ticket sales and popcorn sales
    total_revenue = total_ticket_revenue + total_popcorn_revenue

    # Return the total revenue earned by the theater on Friday night
    result = total_revenue
    return result

print(solution())