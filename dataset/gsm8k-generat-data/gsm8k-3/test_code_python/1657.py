def solution():
    """Sheila, Purity, and Rose want to rent a house. Sheila has offered to pay five times Purity’s share of the rent. Rose can only afford thrice what Purity pays. If Rose’s share is $1,800, what is the total house rent?"""
    # Define the variables
    p = 1 # Let Purity's share be 1x
    s = 5*p # Sheila will pay 5 times Purity's share
    r = 3*p # Rose will pay 3 times Purity's share

    # Calculate the total share
    total_share = p + s + r

    # Calculate the total rent
    total_rent = 1800 * 3 / total_share

    # Display the total rent
    result = total_rent
    return result

print(solution())