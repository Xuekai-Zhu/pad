def solution():
    # Calculate the total revenue from ticket sales
    ticket_sales = 2520

    # Calculate the number of people who bought tickets
    num_tickets = ticket_sales / 5

    # Calculate the revenue from food, rides, and souvenirs
    food_sales = (2/3) * num_tickets * 8
    ride_sales = (1/4) * num_tickets * 4
    souvenir_sales = (1/8) * num_tickets * 15

    # Calculate the total revenue from all sources
    total_revenue = ticket_sales + food_sales + ride_sales + souvenir_sales

    result = total_revenue
    return result

print(solution())