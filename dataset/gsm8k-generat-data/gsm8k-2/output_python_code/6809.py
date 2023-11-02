def solution():
    """Brenda bakes 20 cakes a day. She does this for 9 days and then sells half of the cakes. How many cakes are left with Brenda?"""
    total_cakes = 20 * 9
    sold_cakes = total_cakes / 2
    remaining_cakes = total_cakes - sold_cakes
    result = remaining_cakes
    return result

print(solution())