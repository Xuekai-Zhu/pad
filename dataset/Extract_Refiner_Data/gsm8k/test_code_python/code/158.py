def solution():
    
    # Define the initial price of a bag of marbles
    initial_price = 20

    # Calculate the price increase every two months
    price_increase = initial_price * 0.2

    # Calculate the new price after two months
    new_price = initial_price + price_increase

    # Calculate the total cost after 36 months
    total_cost = new_price * 36

    # Display the total cost
    result = total_cost
    return result

print(solution())