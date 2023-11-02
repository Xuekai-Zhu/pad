def solution():
    """After shearing her 200 sheep, Azalea paid the shearer who had come to help her with the work $2000 for his job. Each of the sheared sheep produced 10 pounds of wool. If Ms. Azalea sold a pound of wool at $20, how much profit did she make from the produce of her sheep farm?"""
    # Define the number of sheep and the amount paid to the shearer
    num_sheep = 200
    shearer_payment = 2000

    # Calculate the total amount of wool produced
    total_wool = num_sheep * 10

    # Calculate the total revenue from selling the wool
    total_revenue = total_wool * 20

    # Calculate the profit after paying the shearer
    profit = total_revenue - shearer_payment

    # return the result
    result = profit
    return result

print(solution())