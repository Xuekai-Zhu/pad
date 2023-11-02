def solution():
    """Sharon wants to get kitchen supplies. She admired Angela's kitchen supplies which consist of 20 pots, 6 more than three times as many plates as the pots, and half as many cutlery as the plates. Sharon wants to buy half as many pots as Angela, 20 less than three times as many plates as Angela, and twice as much cutlery as Angela. What is the total number of kitchen supplies Sharon wants to buy?"""
    # Define Angela's supply numbers
    angela_pots = 20
    angela_plates = (angela_pots * 3) + 6
    angela_cutlery = angela_plates / 2

    # Define Sharon's supply numbers based on Angela's numbers
    sharon_pots = angela_pots / 2
    sharon_plates = (angela_plates * 3) - 20
    sharon_cutlery = angela_cutlery * 2

    # Calculate the total number of supplies Sharon wants to buy
    total_supplies = sharon_pots + sharon_plates + sharon_cutlery

    # Display the total number of supplies
    result = total_supplies
    return result

print(solution())