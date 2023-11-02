def solution():
    # Calculate the total sales required to make $60000 in a year
    total_sales = 60000
    current_sales = 4000*12  # $4000 worth of shoes sold every month
    required_sales = total_sales - current_sales

    # Calculate the additional monthly sales required
    additional_sales = required_sales / 12
    result = additional_sales
    return result

print(solution())