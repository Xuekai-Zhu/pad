def solution():
    
    # Define the price of brownies and slices of cheesecakes
    BROWNIE_PRICE = 3
    CHEESECAKE_PRICE = 4

    # Define the number of brownies and slices of cheesecakes sold
    brownies_sold = 43
    cheesecakes_sold = 23

    # Calculate the total amount raised
    total_raised = (brownies_sold * BROWNIE_PRICE) + (cheesecakes_sold * CHEESECAKE_PRICE)

    # Display the total amount raised
    result = total_raised
    return result

print(solution())