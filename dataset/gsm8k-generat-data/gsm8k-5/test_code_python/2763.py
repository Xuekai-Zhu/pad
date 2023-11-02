def solution():
    friday_sales = 30  # Markeesha sold 30 boxes on Friday
    saturday_sales = friday_sales * 2  # Markeesha sold twice as many on Saturday as she did on Friday
    sunday_sales = saturday_sales - 15  # Markeesha sold 15 fewer on Sunday than she did on Saturday

    # Calculate total sales over the three days
    total_sales = friday_sales + saturday_sales + sunday_sales
    result = total_sales
    return result

print(solution())