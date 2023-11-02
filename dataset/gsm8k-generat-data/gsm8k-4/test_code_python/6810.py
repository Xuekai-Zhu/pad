def solution():
    """Brenda bakes 20 cakes a day. She does this for 9 days and then sells half of the cakes. How many cakes are left with Brenda?"""
    # Define the initial number of cakes
    cakes = 20 * 9

    # Calculate the number of cakes sold
    sold_cakes = cakes / 2

    # Calculate the number of cakes left with Brenda
    remaining_cakes = cakes - sold_cakes

    # return the result
    result = remaining_cakes
    return result

print(solution())