def solution():
    """The grocery store sells chips for $2 per packet and corn chips for $1.5 per packet. John would like to buy 15 packets of chips, and with the rest of the money he has left, buy as many packets of corn chips as he can. How many packets of corn chips could John buy if he has $45 for his entire purchase?"""
    # Define the prices of chips and corn chips
    chips_price = 2
    corn_chips_price = 1.5

    # Define the number of packets of chips John wants to buy
    chips_packets = 15

    # Define the total amount John has to spend
    total_spending = 45

    # Calculate the total cost of the chips packets
    chips_cost = chips_packets * chips_price

    # Calculate the amount left for buying corn chips
    remaining_amount = total_spending - chips_cost

    # Calculate the number of packets of corn chips John can buy with the remaining amount
    corn_chips_packets = remaining_amount // corn_chips_price

    # Return the result
    result = int(corn_chips_packets)
    return result

print(solution())