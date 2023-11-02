def solution():
    # Mary's expenses
    mary_pasta_cost = 20
    mary_bread_cost = 2
    mary_total_cost = mary_pasta_cost + mary_bread_cost

    # Elle and Andrea's expenses
    soda_cost = 1.5
    num_soda_cans = 4
    chicken_wings_cost = 10
    elle_andrea_total_cost = (soda_cost * num_soda_cans) + chicken_wings_cost
    elle_andrea_split_cost = elle_andrea_total_cost / 2

    # Joe's expenses
    joe_cake_cost = 5

    # Total cost of the party
    total_cost = mary_total_cost + elle_andrea_total_cost + joe_cake_cost

    # Calculate how much more Mary spent than the rest of the firm
    rest_of_firm_cost = elle_andrea_split_cost + joe_cake_cost
    difference = mary_total_cost - rest_of_firm_cost
    result = difference
    return result

print(solution())