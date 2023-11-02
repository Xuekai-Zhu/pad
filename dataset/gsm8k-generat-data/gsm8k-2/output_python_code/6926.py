def solution():
    """The Martin family goes to the mall to get ice cream. A kiddie scoop is $3. A regular scoop is $4. A double scoop is $6. Mr. and Mrs. Martin each get the regular scoop. Their two children each get the kiddie scoop. Their three teenage children each get double scoops. How much money does Mrs. Martin pay the cashier?"""
    regular_scoop_price = 4
    kiddie_scoop_price = 3
    double_scoop_price = 6
    total_regular_scoops = 2
    total_kiddie_scoops = 2
    total_double_scoops = 3 * 2
    total_price = (total_regular_scoops * regular_scoop_price) + \
        (total_kiddie_scoops * kiddie_scoop_price) + \
        (total_double_scoops * double_scoop_price)
    result = total_price
    return result

print(solution())