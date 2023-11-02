def solution():
    """Rodney is a door-to-door salesman trying to sell home security systems. He gets a commission of $25 for each system he sells. He is canvassing a neighborhood of four streets with eight houses each. The first street gave him half the sales that the second street did, while every house on the third street turned him away and the fourth street resulted in only one sale. His total commission was $175. How many security systems did he sell on the second street?"""
    commission_rate = 25
    total_commission = 175
    houses_per_street = 8
    
    # calculate sales on the fourth street
    sales_fourth_street = 1
    commission_fourth_street = sales_fourth_street * commission_rate
    
    # calculate total sales on the first three streets
    total_sales_first_three_streets = total_commission - commission_fourth_street
    houses_first_three_streets = houses_per_street * 3
    
    # calculate sales on the first and second streets combined
    sales_first_and_second_streets = (total_sales_first_three_streets / 2) / houses_per_street
    sales_second_street = sales_first_and_second_streets * 2
    
    result = sales_second_street
    return result

print(solution())