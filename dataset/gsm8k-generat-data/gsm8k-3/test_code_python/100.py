def solution():
    """A craft store makes a third of its sales in the fabric section, a quarter of its sales in the jewelry section, and the rest in the stationery section. They made 36 sales today. How many sales were in the stationery section?"""
    # Define the total number of sales
    total_sales = 36

    # Calculate the number of sales in the fabric section
    fabric_sales = total_sales / 3

    # Calculate the number of sales in the jewelry section
    jewelry_sales = total_sales / 4

    # Calculate the number of sales in the stationery section
    stationery_sales = total_sales - fabric_sales - jewelry_sales

    # return the result
    result = stationery_sales
    return result

print(solution())