def solution():
    """Jeff wanted to rent an apartment to live in for the next 5 years until he finishes his studies. He found a nice apartment next to his school, the owner asks Jeff to pay $300 each month, Jeff agreed, and for the first 3 years everything went fine, but then the owner wanted to raise the price for each month to $350. Jeff agreed again and continued paying until he graduated. How much did Jeff end up paying for the apartment throughout the 5 years?"""
    # Calculate the total cost for the first 3 years
    year1_cost = 12 * 300
    year2_cost = 12 * 300
    year3_cost = 12 * 300
    total_cost_year1_3 = year1_cost + year2_cost + year3_cost

    # Calculate the total cost for the last 2 years
    year4_cost = 12 * 350
    year5_cost = 12 * 350
    total_cost_year4_5 = year4_cost + year5_cost

    # Calculate the total cost for the 5 years
    total_cost = total_cost_year1_3 + total_cost_year4_5

    # Display the total cost
    result = total_cost
    return result

print(solution())