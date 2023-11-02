def solution():
    """Jeff wanted to rent an apartment to live in for the next 5 years until he finishes his studies. He found a nice apartment next to his school, the owner asks Jeff to pay $300 each month, Jeff agreed, and for the first 3 years everything went fine, but then the owner wanted to raise the price for each month to $350. Jeff agreed again and continued paying until he graduated. How much did Jeff end up paying for the apartment throughout the 5 years?"""
    # Define the initial monthly rent and the rent after 3 years
    initial_rent = 300
    rent_after_3_years = 350

    # Calculate the total rent paid for the first 3 years
    rent_for_first_3_years = initial_rent * 12 * 3

    # Calculate the total rent paid for the remaining 2 years
    rent_for_remaining_2_years = rent_after_3_years * 12 * 2

    # Calculate the total rent paid over 5 years
    total_rent = rent_for_first_3_years + rent_for_remaining_2_years

    result = total_rent
    return result

print(solution())