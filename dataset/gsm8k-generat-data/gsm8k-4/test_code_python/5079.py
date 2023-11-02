def solution():
    """Connor is taking his date to the movies. The tickets cost $10.00 each. They decided to get the large popcorn & 2 drink combo meal for $11.00 and each grab a box of candy for $2.50 each. How much will Connor spend on his date?"""
    # Define the cost of the items
    ticket_cost = 10
    combo_cost = 11
    candy_cost = 2.5

    # Calculate the total cost
    total_cost = (2 * ticket_cost) + combo_cost + (2 * candy_cost)

    result = total_cost
    return result

print(solution())