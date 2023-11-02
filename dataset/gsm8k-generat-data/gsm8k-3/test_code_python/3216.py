def solution():
    """For Mother's Day last year, Kyle picked a dozen roses from his garden, but this year, he was only able to pick half the number of roses. If Kyle wants to give his mother a bouquet with twice as many roses as last year and the grocery store sells one rose for $3, how much would Kyle have to spend?"""
    # Define the number of roses picked last year
    roses_last_year = 12

    # Calculate the number of roses picked this year
    roses_this_year = roses_last_year / 2

    # Calculate the number of roses in the bouquet
    roses_bouquet = 2 * roses_last_year

    # Calculate the total cost of the roses from the grocery store
    roses_cost = roses_bouquet * 3

    # Display the total cost of the roses
    result = roses_cost
    return result

print(solution())