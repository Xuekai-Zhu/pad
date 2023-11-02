def solution():
    """Marco owns an ice cream truck. His ice cream cones are $5 each. If his expenses are 80% of total sales for the day, how many ice cream cones would he need to sell to make a $200 profit for the day?"""
    expenses_percent = 0.8
    profit = 200
    cone_price = 5
    total_sales_needed = (profit / (1-expenses_percent)) + (expenses_percent * profit)
    cones_needed = total_sales_needed / cone_price
    result = cones_needed
    return result

print(solution())