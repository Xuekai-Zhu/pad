def solution():
    """Jeff wanted to rent an apartment to live in for the next 5 years until he finishes his studies. He found a nice apartment next to his school, the owner asks Jeff to pay $300 each month, Jeff agreed, and for the first 3 years everything went fine, but then the owner wanted to raise the price for each month to $350. Jeff agreed again and continued paying until he graduated. How much did Jeff end up paying for the apartment throughout the 5 years?"""
    first_price = 300
    second_price = 350
    first_years = 3
    second_years = 2
    total_months = first_years * 12 + second_years * 12
    total_price = first_price * first_years * 12 + second_price * second_years * 12
    result = total_price
    return result

print(solution())