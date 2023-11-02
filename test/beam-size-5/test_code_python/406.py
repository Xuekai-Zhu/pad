def solution():
    
    # Define the prices of each item
    BASKET_PRICE = 3
    DISCOUNT_PER_POUND = 0.5
    MAGnets_PRICE = 0.25

    # Calculate the total cost of the taffy's sale
    taffy_cost = BASKET_PRICE * (1 - DISCOUNT_PER_POUND)

    # Calculate the total cost of the taffy's scooped up pounds
    taffy_cost = 2 * BASKET_PRICE

    # Calculate the total cost of the seashells and magnets
    seashell_cost = 1.5
    magnets_cost = 4 * MAGnets_PRICE

    # Calculate the total cost of the vacation
    total_cost = taffy_cost + seashell_cost + magnets_cost

    # Calculate the amount of money Sally has left
    money_left = 10 - total_cost

    # Display the amount of money Sally has left
    result = money_left
    return result

print(solution())