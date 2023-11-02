def solution():
    """Gabrielle sells eggs. On Monday she sells 5 crates of eggs. On Tuesday she sells 2 times as many crates of eggs as Monday. On Wednesday she sells 2 fewer crates than Tuesday. On Thursday she sells half as many crates of eggs as she sells on Tuesday. How many total crates of eggs does she sell for the 4 days?"""
    # Define the number of crates sold on each day
    monday_sales = 5
    tuesday_sales = 2 * monday_sales
    wednesday_sales = tuesday_sales - 2
    thursday_sales = tuesday_sales / 2

    # Calculate the total sales for the 4 days
    total_sales = monday_sales + tuesday_sales + wednesday_sales + thursday_sales

    # Return the result
    result = total_sales
    return result

print(solution())