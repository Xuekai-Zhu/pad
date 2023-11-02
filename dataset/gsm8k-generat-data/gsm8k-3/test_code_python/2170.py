def solution():
    """One set of barrettes costs $3 each, and one comb costs $1 each. Kristine buys one set of barrettes and one comb. Crystal buys three sets of barrettes and one comb. How much do the two girls spend altogether?"""
    # Define the cost of a set of barrettes and a comb
    BARRETTES_PRICE = 3
    COMB_PRICE = 1

    # Define the number of items purchased by each girl
    kristine_items = 2
    crystal_items = 4

    # Calculate the total cost for Kristine's items
    kristine_cost = kristine_items * (BARRETTES_PRICE + COMB_PRICE)

    # Calculate the total cost for Crystal's items
    crystal_cost = crystal_items * (BARRETTES_PRICE + COMB_PRICE)

    # Calculate the total cost for both girls
    total_cost = kristine_cost + crystal_cost

    # Display the total cost
    result = total_cost
    return result

print(solution())