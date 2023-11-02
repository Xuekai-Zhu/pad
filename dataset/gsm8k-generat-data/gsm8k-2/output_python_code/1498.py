def solution():
    """A taco truck is selling soft tacos for $2 and hard shell tacos for $5 during the lunch rush. The first group of customers is a family that buys four hard shell tacos and three soft tacos. The rest of the customers in the lunch rush only buy two soft tacos each. There were ten customers after the family. How many dollars did the taco truck make during the lunch rush?"""
    hardshell_price = 5
    softshell_price = 2
    family_order = (4 * hardshell_price) + (3 * softshell_price)
    rest_order = 10 * 2 * softshell_price
    total_sales = family_order + rest_order
    result = total_sales
    return result

print(solution())