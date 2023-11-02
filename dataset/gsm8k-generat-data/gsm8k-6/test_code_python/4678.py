def solution():
    # Calculate the total revenue from ticket sales for both showings
    first_showing_revenue = 200 * 25  # 200 people bought tickets at $25 per ticket
    second_showing_revenue = 3 * 200 * 25  # three times as many people showed up for the second showing, so 600 people bought tickets at $25 per ticket
    total_revenue = first_showing_revenue + second_showing_revenue
    result = total_revenue
    return result

print(solution())