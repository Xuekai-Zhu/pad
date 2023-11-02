def solution():
    """Connor is taking his date to the movies.  The tickets cost $10.00 each.  They decided to get the large popcorn & 2 drink combo meal for $11.00 and each grab a box of candy for $2.50 each.  How much will Connor spend on his date?"""
    # Define the cost of each item
    TICKET_PRICE = 10.00
    COMBO_PRICE = 11.00
    CANDY_PRICE = 2.50

    # Define the number of each item purchased
    num_tickets = 2
    num_combos = 1
    num_candies = 2

    # Calculate the total cost of the tickets
    ticket_cost = num_tickets * TICKET_PRICE

    # Calculate the total cost of the combo meals
    combo_cost = num_combos * COMBO_PRICE

    # Calculate the total cost of the candies
    candy_cost = num_candies * CANDY_PRICE

    # Calculate the total cost of the date
    total_cost = ticket_cost + combo_cost + candy_cost

    # Display the total cost
    result = total_cost
    return result

print(solution())