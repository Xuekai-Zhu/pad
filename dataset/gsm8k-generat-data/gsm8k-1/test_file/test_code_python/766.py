def solution():
    """A perfume company is trying to create new scents. They already have 4 vanilla scents and 8 fruity scents available and they need to decide which kind of scent to focus on. They decide to focus on whichever scent sells the most and monitor their number of sales as part of their research. By the end of the day, they sell 5 of each of the vanilla scents and 2 of each of the fruity scents available. How many more vanilla scents sold compared with the fruity scents?"""
    vanilla_scents = 4
    fruity_scents = 8
    vanilla_sales = 5 * vanilla_scents
    fruity_sales = 2 * fruity_scents
    difference = vanilla_sales - fruity_sales
    result = difference
    return result

print(solution())