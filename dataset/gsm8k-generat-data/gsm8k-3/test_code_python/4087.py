def solution():
    """Mitch has saved $20000 to finance his boating hobby. A new boat costs $1500 per foot in length. If Mitch needs to keep $500 for a license and registration, and three times that amount for docking fees, how many feet is the longest boat he can buy?"""
    # Define the cost per foot of the boat and the amounts needed for license, registration, and docking fees
    COST_PER_FOOT = 1500
    LICENSE_REGISTRATION = 500
    DOCKING_FEES = 3 * LICENSE_REGISTRATION

    # Calculate the total amount of money Mitch can spend on the boat
    total_budget = 20000 - LICENSE_REGISTRATION - DOCKING_FEES

    # Calculate the maximum length of the boat Mitch can afford
    max_length = total_budget // COST_PER_FOOT

    # Display the maximum length of the boat
    result = max_length
    return result

print(solution())