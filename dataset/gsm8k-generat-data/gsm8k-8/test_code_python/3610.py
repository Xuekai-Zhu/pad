def solution():
    # Calculate the total cost of Elle and Andrea's drinks and wings
    drinks_and_wings_cost = 4 * 1.5 + 10
    elle_and_andrea_cost = drinks_and_wings_cost / 2

    # Calculate the total cost of all the items bought
    total_cost = 20 + 2 + elle_and_andrea_cost + 5

    # Calculate the total cost for the rest of the firm
    rest_of_firm_cost = elle_and_andrea_cost + 5

    # Calculate the difference in costs
    difference = total_cost - rest_of_firm_cost

    result = difference
    return result

print(solution())