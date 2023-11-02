def solution():
    """Sharon wants to get kitchen supplies. She admired Angela's kitchen supplies which consist of 20 pots, 6 more than three times as many plates as the pots, and half as many cutlery as the plates. Sharon wants to buy half as many pots as Angela, 20 less than three times as many plates as Angela, and twice as much cutlery as Angela. What is the total number of kitchen supplies Sharon wants to buy?"""
    # Define the initial number of pots and plates
    pots = 20
    plates = (pots * 3) + 6

    # Define the number of cutlery
    cutlery = plates / 2

    # Calculate the number of pots Sharon wants to buy
    sharon_pots = pots / 2

    # Calculate the number of plates Sharon wants to buy
    sharon_plates = (plates * 3) - 20

    # Calculate the number of cutlery Sharon wants to buy
    sharon_cutlery = cutlery * 2

    # Calculate the total number of kitchen supplies Sharon wants to buy
    total_supplies = sharon_pots + sharon_plates + sharon_cutlery

    # return the result
    result = total_supplies
    return result

print(solution())