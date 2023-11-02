def solution():
    """Rodney is a door-to-door salesman trying to sell home security systems. He gets a commission of $25 for each system he sells. He is canvassing a neighborhood of four streets with eight houses each. The first street gave him half the sales that the second street did, while every house on the third street turned him away and the fourth street resulted in only one sale. His total commission was $175. How many security systems did he sell on the second street?"""
    commission_per_sale = 25
    total_commission = 175
    total_streets = 4
    houses_per_street = 8

    # Calculate total sales
    third_street_sales = 0
    first_street_sales = 0
    fourth_street_sales = 1
    for street in range(total_streets):
        street_sales = 0
        for house in range(houses_per_street):
            if street == 2:  # Every house on third street turned him away
                continue
            elif street == 0:  # First street sales
                street_sales += 0.5 * second_street_sales
            elif street == 1:  # Second street sales
                second_street_sales = street_sales
                street_sales = houses_per_street * second_street_sales
            elif street == 3:  # Fourth street sales
                street_sales = fourth_street_sales
            total_commission += commission_per_sale * street_sales

    result = second_street_sales
    return result

print(solution())