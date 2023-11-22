def solution():
    
    # Define the initial cost of the house
    house_cost = 400000

    # Calculate the cost of the transfer fees
    transfer_cost = house_cost * 0.75

    # Calculate the cost of the brokerage fees
    brokerage_cost = house_cost * 0.05

    # Calculate the total cost of the payment
    total_cost = house_cost + transfer_cost + brokerage_cost + 250000

    # Display the total cost
    result = total_cost
    return result

print(solution())