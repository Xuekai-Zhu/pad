def solution():
    """Jeff wanted to rent an apartment to live in for the next 5 years until he finishes his studies. He found a nice apartment next to his school, the owner asks Jeff to pay $300 each month, Jeff agreed, and for the first 3 years everything went fine, but then the owner wanted to raise the price for each month to $350. Jeff agreed again and continued paying until he graduated. How much did Jeff end up paying for the apartment throughout the 5 years?"""
    first_three_years = 36 * 300
    remaining_two_years = 24 * 350
    total_cost = first_three_years + remaining_two_years
    result = total_cost
    return result

print(solution())