def solution():
    # Define the number of shoes and jerseys
    num_shoes = 6
    num_jerseys = 4

    # Calculate the total cost of the jerseys
    jersey_cost = (1/4) * num_shoes * num_jerseys

    # Calculate the total cost of the shoes
    shoe_cost = (560 - jersey_cost) / num_shoes

    # Calculate the total price of all the shoes
    total_shoe_price = shoe_cost * num_shoes
    
    result = total_shoe_price
    return result

print(solution())