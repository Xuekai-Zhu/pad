def solution():
    """For Mother's Day last year, Kyle picked a dozen roses from his garden, but this year, he was only able to pick half the number of roses. If Kyle wants to give his mother a bouquet with twice as many roses as last year and the grocery store sells one rose for $3, how much would Kyle have to spend?"""
    # Define the number of roses Kyle picked last year
    last_year_roses = 12

    # Define the number of roses Kyle picked this year
    this_year_roses = last_year_roses / 2

    # Define the number of roses Kyle wants to give his mother
    total_roses = last_year_roses * 2

    # Calculate the total cost of buying the additional roses
    additional_roses = total_roses - this_year_roses
    total_cost = additional_roses * 3

    result = total_cost
    return result

print(solution())