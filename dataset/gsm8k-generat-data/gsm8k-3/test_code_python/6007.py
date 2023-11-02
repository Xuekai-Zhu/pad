def solution():
    """A garden store sells packages of pumpkin seeds for $2.50, tomato seeds for $1.50, and chili pepper seeds for $0.90. Harry is planning to plant three different types of vegetables on his farm. How much will Harry have to spend if he wants to buy three packets of pumpkin seeds, four packets of tomato seeds, and five packets of chili pepper seeds?"""
    # Define the cost of each type of seed package
    PUMPKIN_PRICE = 2.50
    TOMATO_PRICE = 1.50
    CHILI_PRICE = 0.90

    # Define the number of packets of each type of seed Harry wants to buy
    pumpkin_packets = 3
    tomato_packets = 4
    chili_packets = 5

    # Calculate the total cost of the pumpkin seed packets
    pumpkin_cost = pumpkin_packets * PUMPKIN_PRICE

    # Calculate the total cost of the tomato seed packets
    tomato_cost = tomato_packets * TOMATO_PRICE

    # Calculate the total cost of the chili pepper seed packets
    chili_cost = chili_packets * CHILI_PRICE

    # Calculate the total cost of all the seed packets
    total_cost = pumpkin_cost + tomato_cost + chili_cost

    # Display the total cost
    result = total_cost
    return result

print(solution())