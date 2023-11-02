def solution():
    """Mrs. Brynlee reduced the prices of items in her store by 20% after the local government gave small businesses in her county a subsidy. If the price of a shirt in the store was $60 and that of the leather jacket was $90, calculate the amount of money Teagan will pay for buying 5 shirts and 10 leather jackets at the reduced prices."""
    
    # Define the original prices of the shirt and leather jacket
    shirt_price = 60
    jacket_price = 90
    
    # Calculate the reduced prices after the 20% discount
    shirt_discounted = shirt_price * 0.8
    jacket_discounted = jacket_price * 0.8
    
    # Calculate the total cost of buying 5 shirts and 10 leather jackets
    total_cost = (shirt_discounted * 5) + (jacket_discounted * 10)
    
    # Display the total cost
    result = total_cost
    return result

print(solution())