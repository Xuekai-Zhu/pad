def solution():
    theater_capacity = 400
    fill_percentage = 0.8
    ticket_price = 30
    total_shows = 3

    # Calculate the number of tickets sold in one show
    tickets_sold = theater_capacity * fill_percentage

    # Calculate the revenue from one show
    show_revenue = tickets_sold * ticket_price

    # Calculate the total revenue from all shows
    total_revenue = show_revenue * total_shows
    result = total_revenue
    return result

print(solution())