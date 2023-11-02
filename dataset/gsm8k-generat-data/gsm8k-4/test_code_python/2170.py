def solution():
    """One set of barrettes costs $3 each, and one comb costs $1 each. Kristine buys one set of barrettes and one comb. Crystal buys three sets of barrettes and one comb. How much do the two girls spend altogether?"""
    # Define the prices of the barrettes and the comb
    barrettes_price = 3
    comb_price = 1

    # Calculate the total cost of Kristine's purchase
    kristine_cost = barrettes_price + comb_price

    # Calculate the total cost of Crystal's purchase
    crystal_cost = (3 * barrettes_price) + comb_price

    # Calculate the total cost of both purchases
    total_cost = kristine_cost + crystal_cost

    # Return the result
    result = total_cost
    return result

print(solution())