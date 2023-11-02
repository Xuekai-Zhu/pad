def solution():
    # Calculate the total number of visitors in a week
    total_visitors = 100*5 + 200 + 300  # 100 people per day for 5 days, 200 on Saturday, and 300 on Sunday
    # Calculate the total revenue in a week
    total_revenue = total_visitors * 3  # each ticket costs $3
    result = total_revenue
    return result

print(solution())