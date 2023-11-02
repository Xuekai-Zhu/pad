def solution():
    """Mitch has saved $20000 to finance his boating hobby. A new boat costs $1500 per foot in length. If Mitch needs to keep $500 for a license and registration, and three times that amount for docking fees, how many feet is the longest boat he can buy?"""
    # Define the total funds available after deducting the license, registration, and docking fees
    available_funds = 20000 - 500 - (3 * 500)

    # Calculate the maximum length of the boat
    max_length = available_funds / 1500

    # Return the result
    result = max_length
    return result

print(solution())