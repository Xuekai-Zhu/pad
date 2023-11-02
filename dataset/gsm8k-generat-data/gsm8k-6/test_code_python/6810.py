def solution():
    # Calculate the total number of cakes baked by Brenda in 9 days
    total_cakes = 20 * 9

    # Calculate the number of cakes sold by Brenda
    sold_cakes = total_cakes / 2

    # Calculate the number of cakes left with Brenda
    left_cakes = total_cakes - sold_cakes 
    result = left_cakes
    return result

print(solution())