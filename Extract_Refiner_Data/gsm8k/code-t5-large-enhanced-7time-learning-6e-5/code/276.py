def solution():
    
    # Define the cost of each item
    PPAE_PRICE = 0.25
    ICE_CREAM_PRICE = 0.50

    # Define the number of each item purchased
    popsicles = 20
    ice_cream_bars = 4

    # Calculate the total cost of the popsicles
    popsicles_cost = popsicles * PPAE_PRICE

    # Calculate the total cost of the ice cream bars
    ice_cream_cost = ice_cream_bars * ICE_CREAM_PRICE

    # Calculate the total cost of everything
    total_cost = popsicles_cost + ice_cream_cost

    # Display the total cost
    result = total_cost
    return result

print(solution())