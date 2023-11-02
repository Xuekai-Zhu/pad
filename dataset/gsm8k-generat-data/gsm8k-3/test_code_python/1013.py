def solution():
    """Justin bought some jerseys. He bought four long-sleeved ones that cost $15 each, and some striped ones that cost $10 each. How many striped jerseys did Justin buy if he spent a total of $80?"""
    # Define the cost of each type of jersey
    LONG_SLEEVED_PRICE = 15
    STRIPED_PRICE = 10

    # Define the number of each type of jersey purchased
    long_sleeved_count = 4
    striped_count = 0 # initialize striped_count
    total_cost = 80

    # Calculate how many striped jerseys Justin bought
    remaining_cost = total_cost - (long_sleeved_count * LONG_SLEEVED_PRICE)
    if remaining_cost % STRIPED_PRICE == 0:
        striped_count = remaining_cost // STRIPED_PRICE
    else:
        striped_count = remaining_cost // STRIPED_PRICE + 1

    # Display the number of striped jerseys Justin bought
    result = striped_count
    return result

print(solution())