def solution():
    """The grocery store sells chips for $2 per packet and corn chips for $1.5 per packet. John would like to buy 15 packets of chips, and with the rest of the money he has left, buy as many packets of corn chips as he can. How many packets of corn chips could John buy if he has $45 for his entire purchase?"""
    # Define the price of chips and corn chips
    CHIPS_PRICE = 2
    CORN_CHIPS_PRICE = 1.5

    # Define the number of chips John would like to buy
    chips_count = 15

    # Calculate the total cost of the chips
    chips_cost = chips_count * CHIPS_PRICE

    # Calculate the remaining amount John has to spend on corn chips
    remaining_cash = 45 - chips_cost

    # Calculate the number of corn chip packets John can buy
    corn_chips_count = int(remaining_cash / CORN_CHIPS_PRICE)

    # Display the number of corn chip packets John can buy
    result = corn_chips_count
    return result

print(solution())