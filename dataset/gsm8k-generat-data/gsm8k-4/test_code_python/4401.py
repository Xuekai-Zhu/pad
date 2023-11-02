def solution():
    """Alice needs to sell $1000 of shoes to meet her quota. Adidas cost $45, Nike cost $60, and Reeboks cost $35. If she sells 8 Nikes, 6 Adidas's, and 9 Reeboks, how much is she short or above her goal?"""
    # Define the cost of each shoe brand
    ADIDAS_COST = 45
    NIKE_COST = 60
    REEBOK_COST = 35

    # Define the number of shoes sold for each brand
    adidas_sold = 6
    nike_sold = 8
    reebok_sold = 9

    # Calculate the total sales from each brand
    adidas_sales = adidas_sold * ADIDAS_COST
    nike_sales = nike_sold * NIKE_COST
    reebok_sales = reebok_sold * REEBOK_COST

    # Calculate the total sales
    total_sales = adidas_sales + nike_sales + reebok_sales

    # Determine if Alice met her quota, and by how much
    if total_sales >= 1000:
        result = total_sales - 1000
    else:
        result = 1000 - total_sales

    return result

print(solution())