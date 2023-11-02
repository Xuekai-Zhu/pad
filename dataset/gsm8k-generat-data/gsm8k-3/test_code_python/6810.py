def solution():
    """Brenda bakes 20 cakes a day. She does this for 9 days and then sells half of the cakes. How many cakes are left with Brenda?"""
    # Calculate the total number of cakes baked
    total_cakes = 20 * 9

    # Calculate the number of cakes sold
    sold_cakes = total_cakes / 2

    # Calculate the number of cakes left
    left_cakes = total_cakes - sold_cakes

    # Display the number of cakes left
    result = left_cakes
    return result

print(solution())