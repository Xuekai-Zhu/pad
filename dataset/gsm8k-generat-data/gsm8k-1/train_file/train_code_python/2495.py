def solution():
    """This year the Oscar swag bags include two diamond earrings that cost $6,000 each, a new iPhone that costs $2,000, and some designer scarves that each cost $1,500. If the total value of the swag bag is $20,000, how many scarves are there?"""
    diamond_earrings_cost = 6000 * 2
    iphone_cost = 2000
    total_value = 20000
    scarves_value = total_value - diamond_earrings_cost - iphone_cost
    scarves_count = scarves_value / 1500
    result = scarves_count
    return result

print(solution())