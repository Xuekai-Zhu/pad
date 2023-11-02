def solution():
    """Rodney is a door-to-door salesman trying to sell home security systems. He gets a commission of $25 for each system he sells. He is canvassing a neighborhood of four streets with eight houses each. The first street gave him half the sales that the second street did, while every house on the third street turned him away and the fourth street resulted in only one sale. His total commission was $175. How many security systems did he sell on the second street?"""

    # Define the variables
    commission_per_sale = 25
    total_commission = 175
    houses_per_street = 8
    third_street_sales = 0
    fourth_street_sales = 1
    second_street_sales = None

    # Calculate the total number of houses in the neighborhood
    total_houses = houses_per_street * 4

    # Calculate the total number of sales
    total_sales = (total_commission / commission_per_sale)

    # Calculate the total number of sales on the third street
    total_sales -= fourth_street_sales

    # Calculate the total number of sales on the first street
    first_street_sales = second_street_sales / 2
    total_sales -= first_street_sales

    # Subtract the number of houses on the third street from the total houses
    total_houses -= houses_per_street

    # Calculate the number of sales per house on the second street
    sales_per_house = total_sales / total_houses

    # Calculate the number of sales on the second street
    second_street_sales = sales_per_house * houses_per_street

    # Display the number of sales on the second street
    result = second_street_sales
    return result

print(solution())