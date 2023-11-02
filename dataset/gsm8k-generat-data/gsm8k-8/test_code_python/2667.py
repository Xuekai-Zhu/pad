def solution():
    # Calculate Zachary's total sales
    zachary_sales = 40 * 5

    # Calculate Jason's sales as 30% more than Zachary's sales
    jason_sales = 1.3 * zachary_sales

    # Calculate Ryan's sales as $50 more than Jason's sales
    ryan_sales = jason_sales + 50

    # Calculate the total sales of all three friends
    total_sales = zachary_sales + jason_sales + ryan_sales
    result = total_sales
    return result

print(solution())