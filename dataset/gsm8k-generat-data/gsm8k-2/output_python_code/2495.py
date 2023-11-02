def solution():
    """This year the Oscar swag bags include two diamond earrings that cost $6,000 each, a new iPhone that costs $2,000, and some designer scarves that each cost $1,500. If the total value of the swag bag is $20,000, how many scarves are there?"""
    total_value = 20000
    diamond_earring_cost = 6000
    iphone_cost = 2000
    scarf_cost = 1500
    num_diamond_earrings = 2
    num_scarves = (total_value - (num_diamond_earrings * diamond_earring_cost) - iphone_cost) / scarf_cost
    result = num_scarves
    return result

print(solution())