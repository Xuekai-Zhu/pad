def solution():
    """A garden store sells packages of pumpkin seeds for $2.50, tomato seeds for $1.50, and chili pepper seeds for $0.90. Harry is planning to plant three different types of vegetables on his farm. How much will Harry have to spend if he wants to buy three packets of pumpkin seeds, four packets of tomato seeds, and five packets of chili pepper seeds?"""
    # Define the prices of each type of seed
    pumpkin_price = 2.5
    tomato_price = 1.5
    chili_price = 0.9

    # Define the quantities of each type of seed Harry plans to buy
    pumpkin_quantity = 3
    tomato_quantity = 4
    chili_quantity = 5

    # Calculate the total cost of the seeds
    total_cost = (pumpkin_price * pumpkin_quantity) + (tomato_price * tomato_quantity) + (chili_price * chili_quantity)

    # Return the result
    result = total_cost
    return result

print(solution())