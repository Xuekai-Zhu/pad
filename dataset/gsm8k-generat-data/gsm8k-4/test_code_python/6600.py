def solution():
    """Chef Michel made shepherd's pie cut into 4 pieces and chicken pot pie cut into 5 pieces for the lunch crowd.  52 customers ordered slices of shepherd's pie and 80 customers ordered slices of chicken pot pie. How many total pies did Chef Michel sell?"""
    # Define the number of customers who ordered shepherd's pie and chicken pot pie
    shepherd_customers = 52
    chicken_customers = 80

    # Calculate the total number of pieces of shepherd's pie and chicken pot pie sold
    shepherd_pieces = 4 * shepherd_customers
    chicken_pieces = 5 * chicken_customers

    # Calculate the total number of pies sold
    total_pies = (shepherd_pieces + chicken_pieces) / 4

    # return the result
    result = total_pies
    return result

print(solution())