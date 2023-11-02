def solution():
    # Total seats in the theater
    total_seats = 400

    # Percentage of seats filled
    capacity_percent = 0.80

    # Number of seats filled for one show
    seats_filled_one_show = total_seats * capacity_percent

    # Number of tickets sold for one show
    tickets_sold_one_show = seats_filled_one_show

    # Revenue for one show
    revenue_one_show = tickets_sold_one_show * 30

    # Revenue for all three performances
    total_revenue = revenue_one_show * 3
    result = total_revenue
    return result

print(solution())