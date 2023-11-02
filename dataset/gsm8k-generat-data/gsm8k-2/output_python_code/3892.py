def solution():
    """Rocco stores his coins in piles of 10 coins each. He has 4 piles of quarters, 6 piles of dimes, 9 piles of nickels, and 5 piles of pennies. How much money does Rocco have?"""
    quarter_piles = 4
    dime_piles = 6
    nickel_piles = 9
    penny_piles = 5

    # Value of each coin in cents
    quarter_value = 25
    dime_value = 10
    nickel_value = 5
    penny_value = 1

    total_quarters = quarter_piles * 10  # 10 coins per pile
    total_dimes = dime_piles * 10
    total_nickels = nickel_piles * 10
    total_pennies = penny_piles * 10

    # Total value in cents
    total_value = (total_quarters * quarter_value) + (total_dimes * dime_value) + (total_nickels * nickel_value) + (
                total_pennies * penny_value)

    # Convert to dollars
    total_value /= 100.0

    result = total_value
    return result

print(solution())