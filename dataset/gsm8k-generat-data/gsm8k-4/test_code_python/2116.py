def solution():
    """Rodney is a door-to-door salesman trying to sell home security systems. He gets a commission of $25 for each system he sells. He is canvassing a neighborhood of four streets with eight houses each. The first street gave him half the sales that the second street did, while every house on the third street turned him away and the fourth street resulted in only one sale. His total commission was $175. How many security systems did he sell on the second street?"""
    # Define the commission per system and the total commission earned
    COMMISSION_PER_SYSTEM = 25
    TOTAL_COMMISSION = 175

    # Define the number of streets and houses per street
    NUM_STREETS = 4
    HOUSES_PER_STREET = 8

    # Calculate the total number of houses
    total_houses = NUM_STREETS * HOUSES_PER_STREET

    # Calculate the number of sales on the first street
    sales_on_first_street = sales_on_second_street / 2

    # Calculate the number of sales on the third street (which turned him away)
    sales_on_third_street = 0

    # Calculate the number of sales on the fourth street
    sales_on_fourth_street = 1

    # Calculate the number of sales on the second street by using the total commission and subtracting the sales from the other streets
    sales_on_second_street = (TOTAL_COMMISSION - (sales_on_first_street * COMMISSION_PER_SYSTEM) - (sales_on_third_street * COMMISSION_PER_SYSTEM) - (sales_on_fourth_street * COMMISSION_PER_SYSTEM)) / COMMISSION_PER_SYSTEM

    result = round(sales_on_second_street)
    return result

print(solution())