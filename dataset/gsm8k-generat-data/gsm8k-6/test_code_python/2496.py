def solution():
    # Calculate the total cost of the diamond earrings and iPhone
    total_cost_diamonds_and_phone = 2 * 6000 + 2000  # two diamond earrings that cost $6,000 each and a new iPhone that costs $2,000

    # Calculate the total cost of the scarves
    total_cost_scarves = 20000 - total_cost_diamonds_and_phone  # the total value of the swag bag is $20,000

    # Calculate the number of scarves
    num_scarves = total_cost_scarves / 1500  # each designer scarf costs $1,500

    result = num_scarves
    return result

print(solution())