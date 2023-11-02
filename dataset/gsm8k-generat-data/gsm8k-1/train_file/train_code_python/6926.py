def solution():
    """The Martin family goes to the mall to get ice cream. A kiddie scoop is $3. A regular scoop is $4. A double scoop is $6. Mr. and Mrs. Martin each get the regular scoop. Their two children each get the kiddie scoop. Their three teenage children each get double scoops. How much money does Mrs. Martin pay the cashier?"""
    reg_scoop_price = 4
    kids_scoop_price = 3
    double_scoop_price = 6
    
    num_regular_scoops = 2
    num_kids_scoops = 2
    num_double_scoops = 3 * 2
    
    total_cost = (num_regular_scoops * reg_scoop_price) + (num_kids_scoops * kids_scoop_price) + (num_double_scoops * double_scoop_price)
    
    result = total_cost
    
    return result

print(solution())