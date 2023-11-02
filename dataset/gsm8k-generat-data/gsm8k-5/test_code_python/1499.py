def solution():
    # Calculate the total sales from the family's order
    sales_family = (4 * 5) + (3 * 2)  # Four hard shell tacos at $5 each and three soft tacos at $2 each

    # Calculate the total sales from the rest of the customers
    sales_rest = 2 * 3 * 10  # Ten customers each buy 2 soft tacos at $2 each

    # Calculate the total sales during the lunch rush
    total_sales = sales_family + sales_rest
    result = total_sales
    return result

print(solution())