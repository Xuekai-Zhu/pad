def solution():
    ticket_price = 3
    num_days = 7
    num_visitors = [100, 100, 100, 100, 100, 200, 300]  # visitors per day for a week

    # Calculate the total number of visitors for the week
    total_visitors = sum(num_visitors)

    # Calculate the total revenue for the week
    total_revenue = total_visitors * ticket_price
    result = total_revenue
    return result

print(solution())