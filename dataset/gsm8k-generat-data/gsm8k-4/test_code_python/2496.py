def solution():
    """This year the Oscar swag bags include two diamond earrings that cost $6,000 each, a new iPhone that costs $2,000, and some designer scarves that each cost $1,500. If the total value of the swag bag is $20,000, how many scarves are there?"""
    # Define the prices of the items in the swag bag
    earrings_price = 6000
    iphone_price = 2000
    scarf_price = 1500

    # Define the number of earrings and the total cost of the earrings
    num_earrings = 2
    total_earrings_cost = num_earrings * earrings_price

    # Define the total cost of the iPhone
    total_iphone_cost = iphone_price

    # Calculate the remaining value for the scarves
    remaining_value = 20000 - total_earrings_cost - total_iphone_cost

    # Calculate the number of scarves that can be purchased with the remaining value
    num_scarves = remaining_value // scarf_price

    # return the result
    result = num_scarves
    return result

print(solution())