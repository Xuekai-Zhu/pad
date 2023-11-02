def solution():
    diamond_earrings_cost = 6000  # The cost of each diamond earring is $6,000
    iphone_cost = 2000  # The cost of the iPhone is $2,000
    designer_scarf_cost = 1500  # The cost of each designer scarf is $1,500
    total_cost = 20000  # The total value of the swag bag is $20,000

    # Calculate the total cost of the diamond earrings
    total_diamond_earrings_cost = diamond_earrings_cost * 2

    # Calculate the total cost of the iPhone
    total_iphone_cost = iphone_cost * 1

    # Calculate the total cost of the designer scarves
    total_designer_scarf_cost = total_cost - total_diamond_earrings_cost - total_iphone_cost

    # Calculate the number of designer scarves
    num_scarves = total_designer_scarf_cost / designer_scarf_cost
    result = num_scarves
    return result

print(solution())