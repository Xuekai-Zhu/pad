def solution():
    # Define the cost of each shoe brand
    adidas_cost = 45
    nike_cost = 60
    reebok_cost = 35

    # Define the number of shoes sold for each brand
    num_nikes = 8
    num_adidas = 6
    num_reeboks = 9

    # Calculate the total revenue from shoe sales
    total_revenue = (num_nikes * nike_cost) + (num_adidas * adidas_cost) + (num_reeboks * reebok_cost)

    # Calculate how much Alice is above or below her sales goal
    sales_difference = total_revenue - 1000
    result = sales_difference
    return result

print(solution())