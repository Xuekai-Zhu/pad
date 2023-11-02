def solution():
    """After shearing her 200 sheep, Azalea paid the shearer who had come to help her with the work $2000 for his job. Each of the sheared sheep produced 10 pounds of wool. If Ms. Azalea sold a pound of wool at $20, how much profit did she make from the produce of her sheep farm?"""
    # Define the number of sheep and the cost of the shearer's job
    NUM_SHEEP = 200
    SHEARER_COST = 2000

    # Calculate the total amount of wool produced
    total_wool = NUM_SHEEP * 10

    # Calculate the total revenue from selling the wool
    total_revenue = total_wool * 20

    # Calculate the total profit after paying for the shearer's job
    total_profit = total_revenue - SHEARER_COST

    # Display the total profit
    result = total_profit
    return result

print(solution())