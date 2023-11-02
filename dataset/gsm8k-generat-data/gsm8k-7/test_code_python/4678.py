def solution():
    first_show = 200
    second_show = 3 * first_show
    ticket_cost = 25

    # Calculate the total revenue from the first show
    first_show_revenue = first_show * ticket_cost

    # Calculate the total revenue from the second show
    second_show_revenue = second_show * ticket_cost

    # Calculate the total revenue from both shows
    total_revenue = first_show_revenue + second_show_revenue
    result = total_revenue
    return result

print(solution())