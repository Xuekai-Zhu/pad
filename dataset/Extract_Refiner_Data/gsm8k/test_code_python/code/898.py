def solution():
    
    # Define the prices of notebooks and ballpen
    NOTEBOOK_PRICE = 1.5
    BALLPEN_PRICE = 0.5

    # Define the number of notebooks and ballpen purchased
    notebooks_purchased = 5
    ballpen_purchased = 1

    # Calculate the total cost of notebooks and ballpen
    total_cost = (NOTEBOOK_PRICE * notebooks_purchased) + (BALLPEN_PRICE * ballpen_purchased)

    # Display the total cost
    result = total_cost
    return result

print(solution())